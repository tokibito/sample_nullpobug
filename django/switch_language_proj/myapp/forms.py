from django import forms
from django.conf import settings

class SwitchLanguageForm(forms.Form):
    language = forms.ChoiceField(choices=settings.LANGUAGES, required=True)
