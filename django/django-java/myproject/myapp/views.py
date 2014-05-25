# coding: utf-8
import os
import subprocess

from django.conf import settings
from django.http import HttpResponse

JAVA_CMD = 'java'
JAVA_CLASS_PATH = '../java_app/echo.jar'
JAVA_CLASS = 'echo'


def echo(message):
    command = [
        JAVA_CMD,
        '-cp',
        os.path.join(settings.BASE_DIR, JAVA_CLASS_PATH),
        JAVA_CLASS,
        message.encode('utf-8')]
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    proc.wait()
    return proc.stdout.read().decode('utf-8')


def index(request):
    return HttpResponse(echo(u'日本語'))
