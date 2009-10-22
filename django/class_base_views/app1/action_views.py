from django.http import HttpResponse

from core import base_views

def hello_view(request):
    return HttpResponse('Hello world!')

base_views.register(hello_view)
