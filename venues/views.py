from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Venues
from .forms import VenueForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        venue = self.get_object()

        # Retrieve all events held at the venue
        events = venue.events.all()

        context['events'] = events
        return context

