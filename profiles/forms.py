from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    ''' Form to create a profile '''
    class Meta:
        model = Profile
        fields = ['image', 'about', 'real_name']

        labels = {
            'image': 'Profile Picture',
            'real_name': 'Name',
            'about': 'About Me',
        }
