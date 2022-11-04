from django.db import models
from django.urls import reverse

# Create your models here
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    
    # def get_absolute_url(self):
    #     return reverse('/thankyou/')
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
    