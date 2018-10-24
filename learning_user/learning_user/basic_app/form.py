from django import forms
from django.contrib.auth.models import User
from basic_app.models import userProfileInfo

class userForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class userProfileForm(forms.ModelForm):

    class Meta():
        model = userProfileInfo
        fields = ('portofolio_site','profile_pic')
