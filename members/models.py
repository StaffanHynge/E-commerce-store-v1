from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.dispatch import receiver


'''
A members model to maintain information and the members orderhistory
'''
class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phonenumber = models.CharField(max_length=20, null=True, blank=True)
    default_email = models.CharField(max_length=250, null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    billing_adress = models.CharField(max_length=100, null=True, blank=True)
    about = models.CharField(max_length=10000, null=True, blank=True)
    image = ResizedImageField(
        size=[200, None],
        quality=75,
        upload_to="members/",
        force_format="WEBP",
        blank=True,
        null=True,
    )

    def __str__(self): 
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs): 
    '''
    Create or update the user
    '''
    if created: 
        UserProfile.objects.create(user=instance)
        # Existing users just save the profile
        instance.userprofile.save()