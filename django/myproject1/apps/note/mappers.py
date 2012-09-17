from bpmappers.djangomodel import ModelMapper, Mapper, RawField, DelegateField

from apps.note.models import Note
from apps.account.models import User


class NoteUserMapper(ModelMapper):
    class Meta:
        model = User
        fields = ['username']


class NoteMapper(ModelMapper):
    user = DelegateField(NoteUserMapper)

    class Meta:
        model = Note
        fields = ['title', 'text', 'user']
