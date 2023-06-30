from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_resized import ResizedImageField


class Profile(models.Model):
    '''Profile Model'''

    user = models.ForeignKey(
        User, related_name='profile', on_delete=models.CASCADE)
    image = ResizedImageField(
        size=[200, 200],
        quality=75,
        upload_to='profiles/',
        force_format='WEBP',
        blank=False,
    )
    about = models.CharField(max_length=1000, null=True, blank=True)
    real_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    '''Create or update the Profile'''
    if created:
        Profile.objects.create(user=instance)
