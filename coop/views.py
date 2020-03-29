from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # here we display the feed
    return render(request, 'coop/index.html')

def profile(request):
    return render(request, 'coop/profile.html')

def feed(request):
    return HttpResponse("This is the feed page")

def upload(request):
    return render(request, 'coop/upload.html')

def settings(request):
    return render(request, 'coop/settings.html')

def about(request):
    return render(request, 'coop/about.html')