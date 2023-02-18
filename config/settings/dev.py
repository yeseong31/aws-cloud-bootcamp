from dj_database_url import config

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv('LOCAL_DB_ENGINE'),
        'NAME': os.getenv('LOCAL_DB_NAME'),
        'USER': os.getenv('LOCAL_DB_USER'),
        'PASSWORD': os.getenv('LOCAL_DB_PASSWORD'),
        'HOST': os.getenv('LOCAL_DB_HOST'),
        'PORT': int(os.getenv('LOCAL_DB_PORT')),
    },
    # "mongodb": {
    #     "ENGINE": os.getenv('LOCAL_MONGODB_ENGINE'),
    #     'NAME': os.getenv('LOCAL_MONGODB_NAME'),
    #     'USER': os.getenv('LOCAL_MONGODB_USER'),
    #     'PASSWORD': os.getenv('LOCAL_MONGODB_PASSWORD'),
    #     'HOST': os.getenv('LOCAL_MONGODB_HOST'),
    #     'PORT': int(os.getenv('LOCAL_MONGODB_PORT')),
    # }
}

db_from_env = config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
