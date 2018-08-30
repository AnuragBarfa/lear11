from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import NotesForm
from django.shortcuts import render ,get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required
from .models import Note
import requests
from bs4 import BeautifulSoup

# Create your views here.
############# strat views for notes
@login_required
def add_notes(request):
    if request.method == "POST":
        notes_form = NotesForm(request.POST, request.FILES)
        if notes_form.is_valid():
            notes_form = notes_form.save(commit=False)
            notes_form.save()

            return redirect('/student/notes/add/')
    else:
        notes_form = NotesForm()
    return render(request, 'notes/add_notes.html', {'form': notes_form})
@login_required
def all_semester(request):
    semesters = []
    semester_list = []
    all_notes = Note.objects.all()
    for notes in all_notes:
        if not (notes.semester in semester_list):
            semester_list.append(notes.semester)
    semester_list.sort()
    try:
        page = requests.get('https://www.iitg.ac.in/maths/acads/btech_struct.php',verify=False)
        soup = BeautifulSoup(page.text, 'html.parser')
        table_body = soup.find_all('table')[1]  # for getting table of semesters
        rows = table_body.find_all(['tr', 'p'])  # all rows of table of semesters
        subjects = []
        i = 0
        for row in rows:
            # to ignore the row which contain the table of semsters i.e len(row)!=2
            if (len(row) != 2):
                if (len(row) == 1):
                    i = i + 1
                    if (i % 2 != 0):
                        semesters.append(subjects)
                        subjects = []
                else:
                    cols = row.find_all('td')
                    cols = [x.text.strip() for x in cols]
                    subjects.append(cols)
        semesters.append(subjects)
        semesters = semesters[1:]
    except requests.exceptions.RequestException as e:
        for i in range(1,10):
            semesters.append([]);
        for notes in all_notes:
            index=notes.semester[:1]
            if(index=='F'):
                continue
            else:
                index=int(index)-1
            if not ([notes.subject] in semesters[index]):
                semesters[index].append([notes.subject])
    #pass semesters in [ [[],[]] , [[],[]] , [[]] , [[]] ] format
    return render(request, 'notes/all_semester.html', {'semester_list': semester_list, 'semesters': semesters})

@login_required
def all_subjects_in_semester(request,Semester_name):
    Semester_choices = ['1st_semester','2nd_semester','3rd_semester','4th_semester','5th_semester',
                        '6th_semester','7th_semester',  '8th_semester', 'For_All']
    if not Semester_name in Semester_choices:
        return render(request, 'post/error.html')
    all_notes = Note.objects.all().filter(semester=Semester_name)
    subject_list = []
    subject_detail = []
    for notes in all_notes:
        if not (notes.subject in subject_list):
            subject_list.append(notes.subject)
    print(subject_list)
    try:
        page = requests.get('https://www.iitg.ac.in/ramesh_h/tt_next_sem/', verify=False)
        soup = BeautifulSoup(page.text, 'html.parser')
        table_body = soup.find_all('td')
        result = []
        for i in range(0, len(table_body)):
            if (str(table_body[i]) == "<td>B.Tech.</td>"):
                data = ['?', '?', '?', '?', '?']
                # data.append(str(table_body[i+1])[4:len(str(table_body[i+1]))-5])#semester
                data[0] = str(table_body[i + 4])[4:len(str(table_body[i + 4])) - 5]  # course code
                data[1] = str(table_body[i + 5])[4:len(str(table_body[i + 5])) - 5]  # course name
                data[2] = str(table_body[i + 11])[4:len(str(table_body[i + 11])) - 5]  # instructor name
                data[3] = str(table_body[i + 10])[4:len(str(table_body[i + 10])) - 5]  # room no
                data[4] = str(table_body[i + 9])[4:len(str(table_body[i + 9])) - 5]  # credits
                result.append(data)
            i = i + 12
        print(result)


        for subject in subject_list:
            x = [subject, '?', '?', '?', '?']
            for data in result:
                if (str(subject) == str(data[0])):
                    # subject_detail.append(data)
                    x = data
                    break
            subject_detail.append(x)
        print(subject_detail)
    except requests.exceptions.RequestException as e:
        for subject in subject_list:
            subject_detail.append([subject,'XXXX','XXXX','XXXX','XXXX'])
        print(e)
    return render(request,'notes/all_subject_in_semester.html',{'subject_list':subject_list,'subject_detail':subject_detail,'Semester_name':Semester_name})
def all_notes_in_subject(request,Semester_name,Subject_name):
    Semester_choices = ['1st_semester', '2nd_semester', '3rd_semester', '4th_semester', '5th_semester',
                        '6th_semester', '7th_semester', '8th_semester', 'For_All']
    Subject_choices1 = [ 'CH101', 'CH110', 'MA101','MA102', 'CS101', 'EE102', 'MA201',
                         'MA221', 'MA222', 'MA224', 'MA226', 'CS222', 'MA322',
                         'MA372',  'MA321', 'MA351', 'Competitive_coding', 'Machine_learning']

    if not (Semester_name in Semester_choices and Subject_name in Subject_choices1):
        return render(request, 'post/error.html')
    all_notes = Note.objects.all().filter(semester=Semester_name,subject=Subject_name)
    notes=[]
    notes.append(all_notes.filter(type="Before_Midsem_Notes"))
    notes.append(all_notes.filter(type="After_Midsem_Notes"))
    notes.append(all_notes.filter(type="Others"))

    papers = []
    papers.append(all_notes.filter(type="Quiz1_Paper"))
    papers.append(all_notes.filter(type="Midsem_Paper"))
    papers.append(all_notes.filter(type="Quiz2_Paper"))
    papers.append(all_notes.filter(type="Endsem_Paper"))

    return render(request,'notes/all_notes_in_subject.html',{'notes':notes,'papers':papers})

##### end notes view
@login_required
def model_form_upload(request):
    Docs=Note.objects.all()
    print(Docs)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = DocumentForm()
    return render(request, 'notes/model_form_upload.html', {
        'form': form,'Docs':Docs
    })

###########file upload view
# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'core/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'core/simple_upload.html')
#file view end