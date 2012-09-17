# coding: utf-8
import json
from django import http
from django.views.generic import CreateView, DetailView, UpdateView, View
from django.utils.decorators import method_decorator

from newauth.decorators import login_required

from apps.note.models import Note
from apps.note.forms import NoteForm
from apps.note.mappers import NoteMapper


class NoteCreateView(CreateView):
    form_class = NoteForm
    template_name = "note/create.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoteCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.auth_user
        obj.save()
        self.object = obj
        return http.HttpResponseRedirect(self.get_success_url())


class NoteUpdateView(UpdateView):
    form_class = NoteForm
    template_name = "note/edit.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoteUpdateView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Note.objects.filter(user=self.request.auth_user)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.auth_user
        obj.save()
        self.object = obj
        return http.HttpResponseRedirect(self.get_success_url())


class NoteDetailView(DetailView):
    template_name = "note/detail.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoteDetailView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Note.objects.filter(user=self.request.auth_user)


class NoteJsonView(View):
    def get(self, *args, **kwargs):
        try:
            obj = Note.objects.get(pk=kwargs.get('pk'))
        except Note.DoesNotExist:
            raise http.Http404
        data = NoteMapper(obj).as_dict()
        return http.HttpResponse(json.dumps(data, indent=2), content_type="application/json")
