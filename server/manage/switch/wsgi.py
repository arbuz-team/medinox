"""
WSGI config for arbuz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/internet/medinox')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.manage.switch.settings")

application = get_wsgi_application()

