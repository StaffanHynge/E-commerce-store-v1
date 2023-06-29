from django import forms
from django.forms import DateInput, TimeInput
from djrichtextfield.widgets import RichTextWidget
from .models import Events


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInout(forms.TimeInput):
    input_type = 'time'


class EventForm(forms.ModelForm):
    """ A form to create an event"""

    class Meta:
        model = Events
        fields = ['name', 'description', 'price',
                  'location', 'date', 'time', 'image', ]
        description = forms.CharField(widget=RichTextWidget())

        widgets = {
            "date": DateInput(),
            "time": TimeInput()
        }

        labels = {
            "title": "Event Title",
            "description": "Description",
            "price": "Price",
            "location": "Location",
            "date": "Date",
            "time": "Time",
            "image": "Image",
        }
