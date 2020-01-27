from os import environ as env

from .base import *

DEBUG = False

SECRET_KEY = env['SECRET_KEY']

ALLOWED_HOSTS = ['*']

MEDIA_ROOT = pathlib.Path(env['MEDIA_ROOT'])
STATIC_ROOT = pathlib.Path(env['STATIC_ROOT'])
LOG_DIR = pathlib.Path(env['LOG_DIR'])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env['DB_NAME'],
        'USER': env['DB_USER'],
        'PASSWORD': env['DB_PASSWORD'],
        'HOST': env['DB_HOST'],
        'PORT': env['DB_PORT'],
    }
}
