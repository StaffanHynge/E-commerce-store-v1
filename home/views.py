from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')

def subscribe(request):
    return render(request, 'home/subscribe.html')

def gallery(request):
    return render(request, 'home/gallery.html')

def test1(request):
    return render(request, 'home/test.html')

def error(request):
    return render(request, 'home/error.html')



