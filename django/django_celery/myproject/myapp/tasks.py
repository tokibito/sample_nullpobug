from celery import shared_task

from .models import Message


@shared_task
def create_message(body):
    Message.objects.create(body=body)
