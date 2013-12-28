from django import forms
from django.forms import formsets
from django.forms import models

from .models import Item

# モデルからModelFormSetの生成を行うmodelformset_factoryを使う場合
ItemFormSet = models.modelformset_factory(Item, extra=1)

# modelformset_factoryを使わない場合
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item

ItemFormSet2 = formsets.formset_factory(ItemForm, extra=1, formset=models.BaseModelFormSet)
ItemFormSet2.model = Item
