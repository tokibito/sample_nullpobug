# coding: utf8
from django import forms

from guestbook.models import Greeting

class GreetingForm(forms.ModelForm):
    """
    ゲストブックの書き込みフォーム
    モデルを元に生成する
    """
    class Meta:
        model = Greeting
 
        # 書き込み日時は除く
        exclude = ('create_at',)

class GreetingForm2(forms.ModelForm):
    """
    ModelFormを使わない場合
    """
    username = forms.CharField(max_length=30)
    content = forms.CharField(max_length=1000, widget=forms.Textarea)
