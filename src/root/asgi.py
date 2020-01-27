import os

from django.core.asgi import get_asgi_application

assert 'DJANGO_SETTINGS_MODULE' in os.environ, '`DJANGO_SETTINGS_MODULE` can not be empty'

application = get_asgi_application()
