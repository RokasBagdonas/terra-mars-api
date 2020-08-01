from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES["default"] = {
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": "test",
    "USER": "test",
    "PASSWORD": "test",
    "HOST": "test-db",
    "PORT": 5432,
}
