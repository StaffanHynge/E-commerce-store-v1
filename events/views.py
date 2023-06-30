from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
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
    success_url = '/events/eventlist/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddEvent, self).form_valid(form)


class EditEvent(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'events/edit_event.html'
    model = Events
    form_class = EventForm
    success_url = '/events/eventlist/'

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteEvent(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete an Event"""
    model = Events
    success_url = '/events/eventlist/'

    def test_func(self):
        return self.request.user == self.get_object().user
