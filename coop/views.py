from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import NoteForm
from .models import Notes, Profile


def index(request):
    # here we display the feed
    return render(request, 'coop/index.html')

def profile(request):
    return render(request, 'coop/profile.html')

def feed(request):
    return render(request, 'coop/feed.html')

def upload(request):
    return render(request, 'coop/upload.html')

def settings(request):
    return render(request, 'coop/settings.html')

def subscriptions(request):
    return render(request, 'coop/subscriptions.html')

# for the search engine
def notes_list(request):
    notes = Notes.objects.all()
    return render(request, 'coop/notes_list.html', {
        'notes': notes
    })
def profile_list(request):
    profile = Profile.objects.all()
    return render(request, 'coop/profile.html', {
        'profile': profile
    })

# for user specific notes feed
def userNotes(request):
    notes = Notes.objects.filter(created_by=request.user.username)
    return render(request, 'coop/userNotes.html', {
        'notes': notes
    })

# upload a note
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            fs = form.save()
            fs.created_by = request.user.username
            fs.save()
            return redirect('userNotes') # Redirects to notes list after uploading
    else:
        form = NoteForm()
    return render(request, 'coop/upload_note.html', {
        'form': form
    })

# delete a note
def delete_note(request, pk):
    if request.method == 'POST':
        note = Notes.objects.get(pk=pk)
        note.delete()
        return redirect('userNotes')

def about(request):
    return render(request, 'coop/about.html')

def help(request):
    return render(request, 'coop/help.html')
