from django import forms
from django.forms import formsets
from django.forms import models

from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item


# ModelFormをFormSetにするならBaseModelFormSetを継承したクラスにすると便利
ItemFormSet = formsets.formset_factory(ItemForm, extra=1, formset=models.BaseModelFormSet)
ItemFormSet.model = Item
# やってることは同じで別のショートカット関数
ItemFormSet2 = models.modelformset_factory(Item, extra=1)
