from django.shortcuts import render ,get_object_or_404 ,redirect
from django.template.defaultfilters import length
from django.utils import timezone
from .models import Post,Comment,Alumni,Temporary
from student.models import Student
from home.models import Person
from .forms import PostForm,CommentForm,TemporaryForm
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Q
from django.http import HttpResponse
import json
import datetime
#VEDIO_FILE_TYPES = ['webm','wav', 'mp3', 'ogg']


########### alumni view start

@login_required
def alumni_list(request):
    alumnis=Alumni.objects.all()
    posts = Post.objects.filter(published_date__isnull=False).order_by('created_date')
    unapprovedposts = Post.objects.filter(approved_post=False).order_by('created_date')
    unpublishedposts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    if len(unapprovedposts) - len(unpublishedposts) >= 0:
        approvalpending = len(unapprovedposts) - len(unpublishedposts)
    else:
        approvalpending = 0
    # search request result
    query = request.GET.get("q")
    if query:
        alumnis=alumnis.filter(
            Q(name__icontains=query)
            ).distinct()
        return render(request, 'alumni/alumni_list.html', {'alumnis': alumnis,'posts':posts, 'approvalpending': approvalpending})
    return render(request, 'alumni/alumni_list.html', {'alumnis': alumnis,'posts':posts, 'approvalpending': approvalpending})

@login_required
def alumni_detail(request ,pk):
    alumni = get_object_or_404(Alumni, pk=pk)
    unapprovedposts = Post.objects.filter(approved_post=False).order_by('created_date')
    unpublishedposts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    if len(unapprovedposts) - len(unpublishedposts) >= 0:
        approvalpending = len(unapprovedposts) - len(unpublishedposts)
    else:
        approvalpending = 0
    return render(request, 'alumni/alumni_details.html', {'alumni': alumni, 'approvalpending': approvalpending, })
# alumni view end

############ post view start

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('created_date')
    videos=Temporary.objects.all()
    videos=videos[::-1]
    posts=posts[::-1]#for reversing the array
    unapprovedposts = Post.objects.filter(approved_post=False).order_by('created_date')
    unpublishedposts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    if len(unapprovedposts)-len(unpublishedposts)>=0:
        approvalpending=len(unapprovedposts)-len(unpublishedposts)
    else:
        approvalpending=0
    group = request.user.groups.all()
    for g in group:
        if g.name == "Student":
            person = get_object_or_404(Student, person=get_object_or_404(Person,person_user=request.user))
        else:
            person = get_object_or_404(Alumni, person=get_object_or_404(Person,person_user=request.user))
    if request.method == "POST":
        form = CommentForm(request.POST)
        print (request.POST)
        comment_text = request.POST.get("the_post")
        if comment_text!="":
            #to check if comment posted using ajax is not empty
            response_data = {}#this response is the json response we use in ajax post call
            if request.POST.get("pk_id"):
                post=get_object_or_404(Post,pk=request.POST.get("pk_id"))
            else:
                post=get_object_or_404(Post,pk=request.POST.get("butt"))

            print ("comment", comment_text)
            #print (person.profile_img.url)
            comment = Comment(post=post, author=get_object_or_404(Person,person_user=request.user),
                              text=comment_text, created_date=datetime.datetime.now(),
                              approved_comment=True)
            comment.save();
            response_data['result'] = 'Create post successful!'
            response_data['text'] = comment_text
            response_data['author']=get_object_or_404(Person,person_user=request.user).username
            response_data['date']=(datetime.datetime.now()).strftime('%B %d, %Y %I:%M %p')#to convert date time in our required formate
            response_data['author_image']=get_object_or_404(Person,person_user=request.user).person_img.url

            # response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
            # response_data['author'] = post.author
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
    else:
        form = CommentForm()
    return render(request, 'post/post_list.html', {'form':form,'posts': posts,'videos':videos,'approvalpending':approvalpending,'person':person})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            group = request.user.groups.all()
            for g in group:
                if g.name == "Student":
                    person =get_object_or_404(Student,person=get_object_or_404(Person,person_user=request.user))
                else:
                    # print("in alumni")
                    person =get_object_or_404(Alumni,person=get_object_or_404(Person,person_user=request.user))
            post = form.save(commit=False)
            post.author = get_object_or_404(Person,person_user=request.user)
            #post.author_image=person.profile_img
            post.save()
            posts = Post.objects.all()
            return redirect('alumni:post_detail', pk=post.pk)
    else:
        form = PostForm()
    unapprovedposts = Post.objects.filter(approved_post=False).order_by('created_date')
    unpublishedposts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    if len(unapprovedposts) - len(unpublishedposts) >= 0:
        approvalpending = len(unapprovedposts) - len(unpublishedposts)
    else:
        approvalpending = 0
    return render(request, 'post/post_edit.html', {'form': form,'approvalpending':approvalpending,})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user_all_post=Post.objects.filter(author=get_object_or_404(Person,person_user=request.user))
    if post in user_all_post:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = get_object_or_404(Person,person_user=request.user)
                # post.published_date = timezone.now()
                post.save()
                unapprovedposts = Post.objects.filter(approved_post=False).order_by('created_date')
                return redirect('alumni:post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        unapprovedposts = Post.objects.filter(approved_post=False).order_by('created_date')
        unpublishedposts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
        if len(unapprovedposts) - len(unpublishedposts) >= 0:
            approvalpending = len(unapprovedposts) - len(unpublishedposts)
        else:
            approvalpending = 0
        return render(request, 'post/post_edit.html', {'form': form,'approvalpending':approvalpending,})
    else:
        return render(request,'post/error.html')    

@login_required
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    user_all_post=Post.objects.filter(author=get_object_or_404(Person,person_user=request.user))
    user_post=0
    if(post in user_all_post):user_post=1
    print(user_post)
    unapprovedposts = Post.objects.filter(approved_post=False).order_by('created_date')
    unpublishedposts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    if len(unapprovedposts) - len(unpublishedposts) >= 0:
        approvalpending = len(unapprovedposts) - len(unpublishedposts)
    else:
        approvalpending = 0
    return render(request, 'post/post_details.html', {'post': post,'approvalpending':approvalpending,'user_post':user_post,})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    posts = posts.filter(author=get_object_or_404(Person,person_user=request.user))
    unapprovedposts = Post.objects.filter(approved_post=False).order_by('created_date')
    unpublishedposts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    if len(unapprovedposts) - len(unpublishedposts) >= 0:
        approvalpending = len(unapprovedposts) - len(unpublishedposts)
    else:
        approvalpending = 0
    return render(request, 'post/post_draft_list.html', {'posts': posts,'approvalpending':approvalpending,})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    users_all_post = Post.objects.filter(author=get_object_or_404(Person,person_user=request.user))
    if (post in users_all_post):
        post.publish()
        return redirect('alumni:post_detail',pk=pk)
    else:
        return render(request, 'post/error.html')

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    users_all_post = Post.objects.filter(author=get_object_or_404(Person,person_user=request.user))
    if (post in users_all_post):
        post.delete()
        return redirect('alumni:post_list')
    else:
        return render(request, 'post/error.html')
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            group = request.user.groups.all()
            for g in group:
                if g.name == "Student":
                    person =get_object_or_404(Student,person=get_object_or_404(Person,person_user=request.user))
                else:
                    # print("in alumni")
                    person =get_object_or_404(Alumni,person=get_object_or_404(Person,person_user=request.user))
            comment = form.save(commit=False)
            comment.author = get_object_or_404(Person,person_user=request.user)
            comment.post = post
            comment.save()
            return redirect('alumni:post_detail' ,pk=post.pk)
    else:
        form = CommentForm()
    unapprovedposts = Post.objects.filter(approved_post=False).order_by('created_date')
    unpublishedposts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    if len(unapprovedposts) - len(unpublishedposts) >= 0:
        approvalpending = len(unapprovedposts) - len(unpublishedposts)
    else:
        approvalpending = 0
    return render(request, 'post/add_comment_to_post.html', {'form': form,'approvalpending':approvalpending,})

# @login_required
# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     #print ("printing ",post)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         #print(form)
#         group = request.user.groups.all()
#         for g in group:
#             if g.name == "Student":
#                 person =get_object_or_404(Student,person=get_object_or_404(Person,person_user=request.user))
#             else:
#                 # print("in alumni")
#                 person =get_object_or_404(Alumni,person=get_object_or_404(Person,person_user=request.user))
#         print (request.POST)
#         comment_text=request.POST.get("the_post")
#         response_data = {}
#         print ("comment",comment_text)
#         comment=Comment(post=post,author=get_object_or_404(Person,person_user=request.user),text=comment_text,created_date=datetime.datetime.now(),approved_comment=True)
#         comment.save();
#         #print("printing comment")
#         #print(comment)
#         response_data['result'] = 'Create post successful!'
#         response_data['postpk'] = post.pk
#         response_data['text'] = post.text
#         #response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
#         #response_data['author'] = post.author
#         return HttpResponse(
#             json.dumps(response_data),
#             content_type="application/json"
#         )
#
#             # comment = form.save(commit=False)
#             # comment.author = request.user.first_name+" "+request.user.last_name
#             # comment.author_image=person.profile_img
#             # comment.post = post
#             # comment.save()
#             #return redirect('alumni:post_detail' ,pk=post.pk)
#
#     else:
#         form = CommentForm()
#
#     unapprovedposts = Post.objects.filter(approved_post=False).order_by('created_date')
#     unpublishedposts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
#     if len(unapprovedposts) - len(unpublishedposts) >= 0:
#         approvalpending = len(unapprovedposts) - len(unpublishedposts)
#     else:
#         approvalpending = 0
#     return render(request, 'post/add_comment_to_post.html', {'form': form,'approvalpending':approvalpending,})

@login_required
@permission_required('polls.can_vote')
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('alumni:post_detail', pk=comment.post.pk)

@login_required
@permission_required('polls.can_vote')
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('alumni:post_detail' ,pk=comment.post.pk)

@login_required
@permission_required('polls.can_vote')
def post_approval(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('created_date')
    unapprovedposts = Post.objects.filter(approved_post=False).order_by('created_date')
    unpublishedposts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    if len(unapprovedposts) - len(unpublishedposts) >= 0:
        approvalpending = len(unapprovedposts) - len(unpublishedposts)
    else:
        approvalpending = 0
    return render(request, 'post/post_approval.html', {'posts': posts,'approvalpending':approvalpending,})

@login_required
@permission_required('polls.can_vote')
def post_approve(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.approve()
    return redirect('alumni:post_approval')
    # return render(request, 'post/post_list.html', {'posts': posts,'approvalpending':approvalpending,'person':person})
@login_required
@permission_required('polls.can_vote')
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('alumni:post_approval')


#post view end
####### upload video veiw
@login_required
def video_upload(request):
    group = request.user.groups.all()
    for g in group:
        if g.name == "Student":
            return render(request, 'post/error.html')
        else:
            if request.method == 'POST':
                form = TemporaryForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('alumni:post_list')
            else:
                form = TemporaryForm()
            return render(request, 'post/video_upload.html', {
                'form': form
            })


