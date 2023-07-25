from django.urls import path
from .views import contact_us

urlpatterns = [
    path('', contact_us.as_view(), name='contact_us'),
]