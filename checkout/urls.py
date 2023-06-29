
from django.contrib import admin
from django.urls import path
from . import views
from .views import download_order

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('download_order/<order_number>/',
         download_order, name='download_order'),
]
