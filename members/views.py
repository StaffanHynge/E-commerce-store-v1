from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from checkout.models import Order
from events.models import Events
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required


def member(request):
    # Display the members profile
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'members/member.html'
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, template, context)

