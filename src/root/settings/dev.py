from os import environ as env

from .base import *

DEBUG = True

SECRET_KEY = env.get(
    'SECRET_KEY',
    't#8g0zn1wp1y$1^5*8f%mwf7)t)1g*@h@k3rq2ndyh6jd^8t)%'
)

MEDIA_ROOT = pathlib.Path(
    env.get('MEDIA_ROOT', BASE_DIR.joinpath('media_root'))
)

STATIC_ROOT = pathlib.Path(
    env.get('STATIC_ROOT', BASE_DIR.joinpath('static_root'))
)

LOG_DIR = pathlib.Path(env.get('LOG_DIR', BASE_DIR.joinpath('log_dir')))
LOG_DIR.mkdir(parents=True, exist_ok=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.get('DB_NAME', 'app'),
        'USER': env.get('DB_USER', 'app_user'),
        'PASSWORD': env.get('DB_PASSWORD', 'password123'),
        'HOST': env.get('DB_HOST', 'localhost'),
        'PORT': env.get('DB_PORT', '5432'),
    }
}
