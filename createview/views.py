from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .models import Employee
from .forms import EmployeeForm
from django import forms
# Create your views here.
class StudentCreateview(CreateView):
    model=Employee
    fields=['name','email','password']
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        form.fields['email'].widget=forms.EmailInput(attrs={'class':'myclass'})
        form.fields['password'].widget=forms.PasswordInput(attrs={'class':'myclass'})
        return form
    # success_url='/thankyou/'

class EmpForm(FormView):
    form_class=EmployeeForm
    template_name='createview/empform.html'
    success_url='/thankyou/'

class Thankyou(TemplateView):
    template_name='application/thankyou.html'

class StudentDetail(DetailView):
    model=Employee
    template_name='createview/employee_detail.html'