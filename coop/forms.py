from django import forms
from .models import Notes
from django.utils.translation import gettext_lazy as _

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('courseName', 'topic', 'description', 'noteFile')
        labels={
            'courseName': _('Course Name'),
            'noteFile': _("Note File")
        }
