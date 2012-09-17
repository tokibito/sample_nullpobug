# coding: utf-8
from myproject1.settings.staging.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'myproject',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
