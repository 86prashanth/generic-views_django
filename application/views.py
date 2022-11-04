from django.shortcuts import render
from .forms import ContactForm,FeedbackForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.
class Thankyou(TemplateView):
    template_name='application/thankyou.html'
    
class ContactForm(FormView):
    template_name='application/contact.html'
    form_class=ContactForm
    # success_url='/thankyou/'
    def form_valid(self,form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        # return super().form_valid(form)
        return HttpResponse('msg sent')
