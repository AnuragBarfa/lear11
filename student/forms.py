from django import forms

from .models import Student,Note
class StudentProfileForm(forms.ModelForm):
    ##roll number and user name should not be changed
    #here you can create fields to be in your form not depend on model class fields
    name = forms.CharField(max_length=30, required=True)
    email_link = forms.EmailField(required=True)
    fb_link = forms.URLField(required=True)
    ln_link = forms.URLField(required=True)
    phone_no = forms.CharField(required=True)
    profile_img = forms.ImageField(required=True)
    curr_work = forms.CharField(max_length=100, required=True)
    pre_work = forms.CharField(max_length=200, required=True)
    class Meta:
        model=Student
        #fields=('name','email_link','curr_work','prev_work',)
        fields = ('name','profile_img', 'phone_no', 'fb_link', 'ln_link', 'email_link', 'curr_work', 'prev_work',)

class NotesForm(forms.ModelForm):
    # Subject_choices1 = [('', '-------'), ('Bio1', 'Bio1'), ('Cse1', 'Cse1'), ('Math1', 'Math1'), ('Me1', 'Me1')]
    description = forms.CharField(max_length=100, required=True)
    #semester=forms.CharField(max_length=50,choices=Subject_choices1,default=' ')
    #offer_1 = forms.IntegerField( choices=[1,2,3],widget=forms.RadioSelect())
    # CHOICES = [('select1', 'select 1'),
    #            ('select2', 'select 2')]
    #
    # like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Note
        fields = ('semester','subject','type','description','document' )