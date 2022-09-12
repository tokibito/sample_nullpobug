from django.shortcuts import render
from django.views.generic import TemplateView


class TopView(TemplateView):
    template_name = "top.html"
