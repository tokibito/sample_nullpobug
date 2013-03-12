# coding: utf-8
from myproject.settings import *

INSTALLED_APPS += (
    'django_jenkins',
)
JENKINS_TASKS = (
    'django_jenkins.tasks.django_tests',
)
PROJECT_APPS = (
    'guestbook',
)
