# coding: utf-8
from myproject1.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('dev', 'dev-myproject1@beproud.jp'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = '/home/www/staticfiles/'

SECRET_KEY = 'secret'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '127.0.0.1:11211',
        ],
    }
}
