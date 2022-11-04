from django.urls import path
from .views import *

urlpatterns = [
    path('',Studentcreateview.as_view(),name='create'),
    path('<int:pk>/',StudentUpdateview.as_view(),name='update'),
    path('thankyou/',Thankyou.as_view(),name='thankyou'),
    path('update/<int:pk>/',Studentupdateform.as_view(),name='update_form'),
]
