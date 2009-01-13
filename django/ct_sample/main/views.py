# coding: utf-8
from django.views.generic.list_detail import object_list
from multicontents.models import MultiContentItem, SimpleMemoItem
from main.models import Event

def index(request):
    return object_list(request, 
                       queryset=MultiContentItem.objects.all(),
                       template_name='index.html')
