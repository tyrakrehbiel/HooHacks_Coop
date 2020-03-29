from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import NoteForm
from .models import Notes


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

def notes_list(request):
    notes = Notes.objects.all()
    return render(request, 'coop/notes_list.html', {
        'notes': notes
    })

def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notes_list') # Redirects to notes list after uploading
    else:
        form = NoteForm()
    return render(request, 'coop/upload_note.html', {
        'form': form
    })

def delete_note(request, pk):
    if request.method == 'POST':
        note = Notes.objects.get(pk=pk)
        note.delete()
        return redirect('notes_list')
