from django.db import models


class Contact(models.Model): 
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=250)
    subject = models.TextField(max_length=100000) 

    def __str__(self):
        return self.name

