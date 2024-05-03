from django.shortcuts import render
from django import forms
from .forms import create_form


def index(request):
    form_class = create_form(
        {
            "name": {"max_length": 100},
            "email": {"max_length": 100},
            "message": {"widget": forms.Textarea},
        }
    )
    form = form_class()
    return render(request, "index.html", {"form": form})
