from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }