from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # here we display the feed
    return HttpResponse("This is the home page")

def profile(request):
    return HttpResponse("This is the profile page")

def feed(request):
    return HttpResponse("This is the feed page")

def upload(request):
    return HttpResponse("This is the page to upload notes documents")

def settings(request):
    return HttpResponse("This is the settings page")