from django.shortcuts import render
from django.utils import translation
from . import forms

def index(request):
    form = forms.SwitchLanguageForm(request.POST or None)
    if form.is_valid():
        lang = form.cleaned_data['language']
        # リクエスト中の言語設定切り替え
        translation.activate(lang)
        # セッションの言語設定切り替え
        request.session['django_language'] = lang
    return render(request, 'index.html', {'form': form})
