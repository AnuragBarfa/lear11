from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
# Create your models here.
curr=datetime.datetime.now().year
YEARS=[]
for i in range(1997 ,curr+4):
    dum=[(i, str(i))]
    YEARS=YEARS+dum
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank = True)
    roll_no=models.IntegerField(default=160123005, blank=True,)
    phone_no=models.IntegerField(default=999999999, blank=True,)
    profile_img = models.ImageField(upload_to='profile_img', default="profile_img/profile.png")
    passout_year = models.IntegerField(default=2016, blank=True, choices=YEARS)
    email_link= models.EmailField(null=True)
    fb_link = models.URLField(null=True)
    ln_link = models.URLField(null=True)
    curr_work = models.CharField(max_length=100, blank = True)
    prev_work = models.CharField(max_length=200, blank = True)
    def __str__(self):
        return self.name