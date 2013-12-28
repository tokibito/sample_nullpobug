from django.shortcuts import render, redirect

from . import forms


def index(request):
    """ModelFormSetを使うと一括データ編集のフォームを簡単に作れる
    """
    formset = forms.ItemFormSet(request.POST or None)
    if formset.is_valid():
        # BaseModelFormSetを継承している場合はsaveメソッドを呼んで保存できる
        formset.save()
        return redirect('index')
    return render(request, 'index.html', {'formset': formset})
