from django.urls import path
from .views import AddEvent, EventList, EventDetail, DeleteEvent, EditEvent

urlpatterns = [
    path('', AddEvent.as_view(), name='add_event'),
    path('eventlist/', EventList.as_view(), name='event_list'),
    path('<int:pk>/', EventDetail.as_view(), name='event_detail'),
    path('delete/<int:pk>/', DeleteEvent.as_view(), name='delete_event'),
    path('edit/<int:pk>/', EditEvent.as_view(), name='edit_event'),
]
