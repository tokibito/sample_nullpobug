from django.http import HttpResponse
from django.shortcuts import render

from .models import Message
from . import tasks 


def create_message(request):
    tasks.create_message.delay(request.GET.get('body'))
    return render(request, 'create_message.html')


def list_message(request):
    return render(request, 'list_message.html',
                  {'messages': Message.objects.all()})
