from django import forms
from django.contrib.auth.models import User,Group
from alumni.models import Alumni
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    group=forms.ModelChoiceField(queryset=Group.objects.all(),required=True)
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)#inbuilt user field
    last_name = forms.CharField(max_length=30, required=True)#inbuilt user field
    email=forms.EmailField(required=True)#inbuilt user field
    image=forms.ImageField()
    fb_link = forms.URLField(required=True)
    ln_link = forms.URLField(required=True)
    phone_no=forms.CharField(required=True)
    curr_work = forms.CharField(max_length=100, required=True)
    pre_work = forms.CharField(max_length=200, required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','phone_no','email','fb_link','ln_link','curr_work','pre_work','username','password','group',]

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.username=self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.ln_link = self.cleaned_data["ln_link"]
        user.fb_link = self.cleaned_data["fb_link"]
        user.phone_no=self.cleaned_data["phone_no"]
        user.curr_work = self.cleaned_data["curr_work"]
        user.pre_work = self.cleaned_data["pre_work"]
        if commit:
            user.save()
        return user