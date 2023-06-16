from django.urls import path
from .views import AddEvent, EventList, EventDetail

urlpatterns = [
    path('', AddEvent.as_view(), name='add_event'),
    path('eventlist/', EventList.as_view(), name='event_list'),
    path('<int:pk>/', EventDetail.as_view(), name='event_detail'),
]
