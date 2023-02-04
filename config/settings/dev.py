from dj_database_url import config

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-83rq50$rrsyoxxa1dwnlhwd!7v@n(!jqn54qemz2w@z^_%d@p@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

db_from_env = config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
