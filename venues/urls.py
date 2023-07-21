from django.urls import path
from .views import AddVenue, VenueList, VenueDetail, DeleteVenue, EditVenue


urlpatterns = [
    path('', AddVenue.as_view(), name='add_venue'),
    path('venuelist/', VenueList.as_view(), name='venue_list'),
    path('<int:pk>/', VenueDetail.as_view(), name='venue_detail'),
    path('delete/<int:pk>/', DeleteVenue.as_view(), name='delete_venue'),
    path('edit/<int:pk>/', EditVenue.as_view(), name='edit_venue'),
]


