# coding: utf-8

from django.views.generic import TemplateView

from myapp.mappers import MyMapper
from myapp.models import C


class MyView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        context['data'] = [MyMapper(obj).as_dict() for obj in C.objects.all()[:5]]
        return context
