# coding: utf-8
from django.forms import ModelForm

from apps.note import models as note_models


class NoteForm(ModelForm):
    class Meta:
        model = note_models.Note
        fields = ['title', 'text']
