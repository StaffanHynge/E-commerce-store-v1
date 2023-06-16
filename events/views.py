from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Events
from .forms import EventForm


class EventList(ListView):
    """View all Events"""
    template_name = 'events/events.html'
    model = Events
    context_object_name = 'events'


class EventDetail(DetailView):
    """Allows user to see the detail of the event"""
    template_name = 'events/event_detail.html'
    model = Events
    context_object_name = 'event'



class AddEvent(LoginRequiredMixin, CreateView):
    template_name = 'events/add_event.html'
    model = Events
    form_class = EventForm
    success_url = '/events/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddEvent, self).form_valid(form)
