from django_resized import ResizedImageField
from djrichtextfield.models import RichTextField
from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    user = models.ForeignKey(
        User, related_name='event_owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=254,)
    description = models.CharField(max_length=10000,)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=254)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="events/",
        force_format="WEBP",
        blank=False,
        null=False,
    )

    def __str__(self):
        return (self.name)
