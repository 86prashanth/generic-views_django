from django.urls import path
from .views import *

urlpatterns = [
    path('',StudentCreateview.as_view(),name='stucreateview'),
    path('thankyou/',TemplateView.as_view(),name='thankyou'),
    path('<int:pk>/',StudentDetail.as_view(),name='detail'),
    path('form',EmpForm.as_view(),name='form'),
]
