from django import forms


FAVORITE_COLORS_CHOICES = {
    "blue": "Blue",
    "green": "Green",
    "black": "Black",
}


class MyForm(forms.Form):
    name = forms.CharField(label="名前")
    body = forms.CharField(label="本文", widget=forms.Textarea)
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
