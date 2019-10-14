# flake8: noqa
from settings.base import *

DEBUG = False
SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())
SECURE_SSL_REDIRECT = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": config("MEMCACHED_LOCATION"),
    }
}

ENV_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
STATIC_ROOT = os.path.join(ENV_PATH, "../public/static/")
MEDIA_ROOT = os.path.join(ENV_PATH, "../public/media/")
