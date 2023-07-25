from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
 
# Create your views here


class ContactUsView(FormView):
    template_name = 'contact/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
