
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('gallery/', views.gallery, name='gallery'),
    path('error/', views.gallery, name='error')
    
]
