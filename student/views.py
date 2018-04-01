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
    page = requests.get('https://www.iitg.ac.in/maths/acads/btech_struct.php',verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    table_body =soup.find_all('table')[1]#for getting table of semesters
    rows = table_body.find_all(['tr', 'p'])#all rows of table of semesters
    semesters=[]
    subjects=[]
    i=0
    for row in rows:
        #to ignore the row which contain the table of semsters i.e len(row)!=2
        if(len(row)!=2):
            if(len(row)==1):
                i=i+1
                if(i%2!=0):
                    semesters.append(subjects)
                    subjects=[]
            else:
                cols = row.find_all('td')
                cols = [x.text.strip() for x in cols]
                subjects.append(cols)
    semesters.append(subjects)
    semesters=semesters[1:]
    #print(semesters)
    all_notes=Note.objects.all()
    semester_list=[]
    for notes in all_notes:
        if not(notes.semester in semester_list):
            semester_list.append(notes.semester)
    semester_list.sort()
    #print(semester_list)
    return render(request, 'notes/all_semester.html',{'semester_list':semester_list,'semesters':semesters})
@login_required
def all_subjects_in_semester(request,Semester_name):
    all_notes=Note.objects.all().filter(semester=Semester_name)
    subject_list=[]
    for notes in all_notes:
        if not(notes.subject in subject_list):
            subject_list.append(notes.subject)
    return render(request,'notes/all_subject_in_semester.html',{'subject_list':subject_list,'Semester_name':Semester_name})
def all_notes_in_subject(request,Semester_name,Subject_name):
    all_notes = Note.objects.all().filter(semester=Semester_name,subject=Subject_name)
    notes=[]
    papers=[]
    # Type_choices = [('', '-------'), ('Before_Midsem_Notes', 'Before_Midsem_Notes'), ('Quiz1_Paper', 'Quiz1_Paper'),
    #                 ('Midsem_Paper', 'Midsem_Paper'), ('After_Midsem_Notes', 'After_Midsem_Notes'),
    #                 ('Quiz2_Paper', 'Quiz2_Paper'), ('Endsem_Paper', 'Endsem_paper'), ('Others', 'Others')]

    notes.append(all_notes.filter(type="Before_Midsem_Notes"))
    notes.append(all_notes.filter(type="After_Midsem_Notes"))
    notes.append(all_notes.filter(type="Others"))
    #print(notes)
    papers.append(all_notes.filter(type="Quiz1_Paper"))
    papers.append(all_notes.filter(type="Midsem_Paper"))
    papers.append(all_notes.filter(type="Quiz2_Paper"))
    papers.append(all_notes.filter(type="Endsem_Paper"))
    #print(papers)
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