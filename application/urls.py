from .views import *
from django.urls import path

urlpatterns = [
    path('',ContactForm.as_view(),name='contact'),
    path('thankyou/',Thankyou.as_view(),name='thankyou'),
]
