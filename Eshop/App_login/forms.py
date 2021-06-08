from django import forms
from App_login.models import Userprofile, Profile
from django.contrib.auth.forms import UserCreationForm



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = Userprofile
        fields = ('email', 'password1', 'password2',)