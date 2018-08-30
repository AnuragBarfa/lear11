from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from home.models import Person
import datetime
from .validators import file_size
class Post(models.Model):
    author = models.ForeignKey('home.Person',on_delete=models.CASCADE)
    #author_image= models.ImageField(upload_to='profile_img', default="profile_img/profile.png")
    title = models.CharField(max_length=200)
    text = models.TextField()
    approved_post = models.BooleanField(default=False)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve(self):
        self.approved_post = True
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('alumni.Post', related_name='comments',on_delete=models.CASCADE)
    author=models.ForeignKey('home.Person',related_name='comments',on_delete=models.CASCADE,null=True)
    #author = models.CharField(max_length=200,blank=True, null=True)
    #author_image = models.ImageField(upload_to='profile_img', default="profile_img/profile.png",blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now,blank=True, null=True)
    approved_comment = models.BooleanField(default=True,blank=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

curr=datetime.datetime.now().year
YEARS=[]
for i in range(1997 ,curr+4):
    dum=[(i, str(i))]
    YEARS=YEARS+dum
class Alumni(models.Model):
    person = models.OneToOneField('home.Person', on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100, blank = True)
    passout_year = models.IntegerField(default=2016, blank=True, choices=YEARS)
    curr_work = models.CharField(max_length=100, blank = True)
    prev_work = models.CharField(max_length=200, blank = True)
    # email_link= models.EmailField(null=True)
    # fb_link = models.URLField(null=True)
    # ln_link = models.URLField(null=True)
    # roll_no=models.IntegerField(default=160123005, blank=True,)
    # phone_no=models.IntegerField(default=999999999, blank=True,)
    # profile_img = models.ImageField(upload_to='profile_img', default="profile_img/profile.png")
    def __str__(self):
        return self.name



class Temporary(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='Alumni_videos/0',validators=[file_size])
    uploaded_at = models.DateTimeField(auto_now_add=True)



