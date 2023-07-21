from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Venues(models.Model): 
    user = models.ForeignKey(User, related_name='venueowner', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    home_page = models.URLField()
    social_media = models.URLField()
    city = models.CharField(max_length=250)
    country = CountryField(blank_label='Country', null=True, blank=True)
    name = models.CharField(max_length=250, null=True)
    image = ResizedImageField(
        size=[200, 200],
        quality=75,
        upload_to='venues/',
        force_format='WEBP',
        blank=False,
    )

    def __str__(self):
        return str(self.user.username)

