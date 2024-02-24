
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('processa_formulario', views.processa_formulario, name="processa_formulario"),
    
]
