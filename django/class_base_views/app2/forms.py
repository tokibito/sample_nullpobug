from django import forms

class MyForm(forms.Form):
    comment = forms.CharField()
