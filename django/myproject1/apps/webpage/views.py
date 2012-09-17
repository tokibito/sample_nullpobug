# coding: utf-8
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from newauth.decorators import login_required


class HomeView(TemplateView):
    template_name = 'home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        from apps.note import api as note_api
        return {'notes': note_api.get_notes(self.request.auth_user)}
