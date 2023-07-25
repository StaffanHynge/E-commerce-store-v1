from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
 
# Create your views here.
def contact_us(request): 

    form  = ContactForm()
    context = ('form': form)
    return render(request,'contact.html',context)