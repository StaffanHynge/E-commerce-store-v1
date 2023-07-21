from django.urls import path
from .views import AddVenue


urlpatterns = [
    path('', AddVenue.as_view(), name='add_venue'),
]

