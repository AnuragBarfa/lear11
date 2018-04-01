from django import forms

from .models import Post,Comment,Alumni,Temporary

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class AlumniProfileForm(forms.ModelForm):
    ##roll number and user name should not be changed
    name = forms.CharField(max_length=30, required=True)
    email_link = forms.EmailField(required=True)
    fb_link = forms.URLField(required=True)
    ln_link = forms.URLField(required=True)
    phone_no = forms.CharField(required=True)
    curr_work = forms.CharField(max_length=100, required=True)
    pre_work = forms.CharField(max_length=200, required=True)
    class Meta:
        model=Alumni
        fields = ('name', 'profile_img', 'phone_no', 'fb_link', 'ln_link', 'email_link', 'curr_work', 'prev_work',)
class TemporaryForm(forms.ModelForm):
    class Meta:
        model = Temporary
        fields = ('description', 'document', )