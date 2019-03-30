from .base import *

DEBUG = False
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
SECURE_SSL_REDIRECT = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}

ENV_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(ENV_PATH, '../public/static/') 
MEDIA_ROOT = os.path.join(ENV_PATH, '../public/media/') 