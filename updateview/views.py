from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import Student
from django import forms
from .forms import Studentform
from django.views.generic.base import TemplateView
# Create your views here.
class Studentcreateview(CreateView):
    model=Student
    fields=['name','email','password']
    success_url='/thankyou/'
    
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['email'].widget=forms.EmailInput(attrs={'class':'myclass'})
        form.fields['password'].widget=forms.PasswordInput(attrs={'class':'myclass'})
        return form
    
class StudentUpdateview(UpdateView):
    model=Student
    fields=['name','email','password']
    success_url='/thankyou/'
    
class Thankyou(TemplateView):
    template_name='updateview/thankyou_update.html'


class Studentupdateform(UpdateView):
    form_class=Studentform
    model=Student
    template_name='updateview/student_form.html'