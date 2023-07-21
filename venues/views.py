from django.shortcuts import render
from django.views.generic import CreateView
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
    """View all Events"""
    template_name = 'venues/venues.html'
    model = Venues
    context_object_name = 'venues'
