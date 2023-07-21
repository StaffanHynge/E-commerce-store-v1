from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Venues
from .forms import VenueForm
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

# Create your views here.


class AddVenue(CreateView):
    template_name = 'venues/add_venue.html'
    model = Venues
    form_class = VenueForm
    success_url = '/venues/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddVenue, self).form_valid(form)


class VenueList(ListView):
    template_name = 'venues/venues.html'
    model = Venues
    context_object_name = 'venues'


class VenueDetail(DetailView):
    template_name = 'venues/venue_detail.html'
    model = Venues
    context_object_name = 'venue'


class EditVenue(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'venues/edit_venue.html'
    model = Venues
    form_class = VenueForm
    success_url = '/venues/venuelist/'

    def test_func(self):
        return self.request.user == self.get_object().user

class DeleteVenue(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Venues
    success_url = '/venues/venuelist/'

    def test_func(self):
        return self.request.user == self.get_object().user
