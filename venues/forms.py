from django import forms
from .models import Venues
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class VenueForm(forms.ModelForm):
    country = CountryField(blank_label='Country', null=True,
                           blank=True).formfield(widget=CountrySelectWidget)

    class Meta:
        model = Venues
        fields = ['image', 'name', 'address', 'phone_number', 'home_page',
                  'social_media', 'city', 'country']

        labels = {
            "name": "Venue Name",
            "Address": "Venues Address",
            "phone_number": "Phone Number",
            "home_page": "Link to homepage",
            "social_media": "Link to Social Media",
            "city": "City",
            "country": "Country",
            "image": "Image"
        }
