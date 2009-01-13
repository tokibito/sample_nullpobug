# coding: utf-8
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list
from django.contrib.contenttypes.models import ContentType
from multicontents.models import MultiContentItem, SimpleMemoItem
from main.models import Event

def index(request, model=None):
    model_class = MultiContentItem
    if model:
        ct = get_object_or_404(ContentType, model=model)
        model_class = ct.model_class()
        if not issubclass(model_class, MultiContentItem):
            raise Http404
    return object_list(request, 
                       queryset=model_class.objects.all(),
                       template_name='index.html',
                       extra_context={'model': model})
