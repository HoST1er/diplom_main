# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FileUploadForm(forms.Form):
    folder = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'type': 'file'}))


class RegisterForm(UserCreationForm):
    model = User