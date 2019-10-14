# flake8: noqa
from .base import *

DEBUG = True
SECRET_KEY = "DEVELOPMENT"  # nosec
ALLOWED_HOSTS = ["*"]

CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}
