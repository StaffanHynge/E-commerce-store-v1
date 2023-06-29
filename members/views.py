from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def member(request):
    # Display the members profile
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'members/member.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)
