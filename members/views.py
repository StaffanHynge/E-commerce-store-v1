from django.shortcuts import render


def member(request): 
    # Display the members profile
    template = 'members/members.html'
    context = {

    }
    return render(request, template, context)