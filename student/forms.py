from django import forms

from .models import Student

class StudentProfileForm(forms.ModelForm):

    class Meta:
        model=Student
        fields=('name','roll_no','profile_img','passout_year','phone_no','fb_link','ln_link','email_link','curr_work','prev_work',)
