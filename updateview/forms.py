from django import forms
from .models import Student


class Studentform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()
    widgets={
        name:forms.TextInput(attrs={'class':'myclass'}),
        email:forms.EmailInput(attrs={'class':'myclass'}),
        password:forms.PasswordInput(render_value=True,attrs={'class':'mypass'}),
    }