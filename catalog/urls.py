from django.urls import path, include
from catalog import views

urlpatterns = [

     path('', views.index, name='index'),
    
]