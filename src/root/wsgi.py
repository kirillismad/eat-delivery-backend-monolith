import os

from django.core.wsgi import get_wsgi_application

assert 'DJANGO_SETTINGS_MODULE' in os.environ, '`DJANGO_SETTINGS_MODULE` can not be empty'

application = get_wsgi_application()
