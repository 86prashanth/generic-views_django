from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView,UpdateView
from .models import Student
from django.urls import reverse
# Create your views here.

class Studentcreate(CreateView):
    model=Student
    fields=['name','email','password']
    success_url='/thankyou/'

class StudentUpdate(UpdateView):
    model=Student
    fields=['name','email','password']
    success_url='/thankyou/'
    
class Studentdelete(DeleteView):
    model=Student
    template_name='deleteview/student_confirm_delete.html'
    success_url='/create/'
    