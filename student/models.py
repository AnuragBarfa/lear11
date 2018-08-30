from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from .validators import validate_file_extension
# Create your models here.
curr=datetime.datetime.now().year
YEARS=[]
for i in range(1997 ,curr+4):
    dum=[(i, str(i))]
    YEARS=YEARS+dum
class Student(models.Model):
    person = models.OneToOneField('home.Person', on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100, blank = True)#blank=true help when you have created some object previously of this class but you have added one new attribute in class now so it will accept empty at thier else so error
    passout_year = models.IntegerField(default=2016, blank=True, choices=YEARS)
    curr_work = models.CharField(max_length=100, blank = True)
    prev_work = models.CharField(max_length=200, blank = True)
    #email_link= models.EmailField(null=True)
    #fb_link = models.URLField(null=True)
    #ln_link = models.URLField(null=True)
    # roll_no=models.IntegerField(default=160123005, blank=True,)
    # phone_no=models.IntegerField(default=999999999, blank=True,)
    # profile_img = models.ImageField(upload_to='profile_img', default="profile_img/profile.png")
    def __str__(self):
        return self.name

# the first choise ('','-------') makes the form filled as compulory to be filled as it has no value
Semester_choices = [('','-------'),('1st_semester','1st_semester'),('2nd_semester','2nd_semester'),('3rd_semester','3rd_semester'),('4th_semester','4th_semester'),('5th_semester', '5th_semester'), ('6th_semester', '6th_semester'), ('7th_semester', '7th_semester'), ('8th_semester', '8th_semester'),('For_All','For_All')]
#whenever choise feild is changed also change the same in student view all_subjects_in_semester and all_notes_in_subject
Subject_choices1=[('','-------'),('CH101','CH101'),('CH110','CH110'),('MA101','MA101'),
                  ('MA102','MA102'),('CS101','CS101'),('EE102','EE102'),
                  ('MA201','MA201'),('MA221','MA221'),('MA222','MA222'),
                  ('MA224','MA224'),('MA226','MA226'),('CS222','CS222'),
                  ('MA322','MA322'),('MA372','MA372'),('MA321','MA321'),('MA351','MA351'),
                  ('Competitive_coding','Competitive_coding'),('Machine_learning','Machine_learning')]
Type_choices=[('','-------'),('Before_Midsem_Notes','Before_Midsem_Notes'),('Quiz1_Paper','Quiz1_Paper'),('Midsem_Paper','Midsem_Paper'),('After_Midsem_Notes','After_Midsem_Notes'),('Quiz2_Paper','Quiz2_Paper'),('Endsem_Paper','Endsem_paper'),('Others','Others')]
class Note(models.Model):
    description = models.CharField(max_length=255)
    document = models.FileField(upload_to='student_notes/',validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    semester=models.CharField(max_length=50,choices=Semester_choices,default=' ')
    subject=models.CharField(max_length=50,choices=Subject_choices1,default=' ')
    type=models.CharField(max_length=50,choices=Type_choices,default=' ')
    video=models.BooleanField(default=False)
    image=models.BooleanField(default=False)
    pdf=models.BooleanField(default=False)
    def __str__(self):
        return self.semester+'-'+self.subject+'-'+self.type

