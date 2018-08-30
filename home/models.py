from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    person_user=models.OneToOneField('auth.User',on_delete=models.CASCADE)
    username = models.CharField(max_length=30, blank=True, default='')
    roll_no=models.IntegerField(default=160123005, blank=True,)
    person_phone_no = models.IntegerField(default=9993993287, blank=True, )
    person_img = models.ImageField(upload_to='profile_img', default="profile_img/profile.png")
    person_email_link = models.EmailField(null=True)
    person_fb_link = models.URLField(null=True)
    person_ln_link = models.URLField(null=True)
    def __str__(self):
        return self.username

