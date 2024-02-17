from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User

from django import forms

class CreateUserForm(UserCreationForm):

    class Meta:
        
        model = User
        fields = ['username','password1','password2']


class LoginForms(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    