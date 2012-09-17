from apps.note.models import Note

def get_notes(user):
    return Note.objects.filter(user=user)
