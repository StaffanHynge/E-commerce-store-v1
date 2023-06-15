from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Events 

class EventForm(forms.ModelForm): 
    """ A form to create an event"""

    class Meta: 
        model = Events
        fields = ['name', 'description', 'price', 'location', 'date', 'time', 'image']
        description = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title" : "Event Title",
            "description" : "Description",
            "price" : "Price",
            "location" : "Location",
            "date" : "Date",
            "time" : "Time",
            "image" : "Image",
        }