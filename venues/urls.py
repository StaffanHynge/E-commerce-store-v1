from django.urls import path
from .views import AddVenue, VenueList, VenueDetail


urlpatterns = [
    path('', AddVenue.as_view(), name='add_venue'),
    path('venuelist', VenueList.as_view(), name='venue_list'),
    path('<int:pk>/', VenueDetail.as_view(), name='venue_detail'),
]

