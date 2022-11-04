from django.urls import path
from .views import *

urlpatterns = [
   
    path('',Studentcreate.as_view(),name='create'),
    path('update/<int:pk>',StudentUpdate.as_view(),name='update'),
    path('delete/<int:pk>',Studentdelete.as_view(),name='delete'),
]
