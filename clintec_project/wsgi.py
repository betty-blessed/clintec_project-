"""
WSGI config for clintec_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clintec_project.settings')

application = get_wsgi_application()


# Web Server Gateway Interface
# Acts as a bridge between a web Server like Apache or Nginx and your Django application
# It is a standard for synchronous web application.
      # Meaning it handles one request/thread at a time. If it takes long to respond (Like slow database query), that thread is blocked until it finishes
# Protocol Support - It is designed for HTTP request.
# Common Servers - Gunicorn, uWSGI & mod_wsgi
# Best for Traditional web apps, standard REST APIs & projects where you dont need real time features like WebSockets