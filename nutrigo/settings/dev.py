from .base import *

DEBUG = True
SECRET_KEY = "DEVELOPMENT_SECRET_KEY"
ALLOWED_HOSTS = ['*']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}