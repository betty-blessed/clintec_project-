"""
ASGI config for clintec_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clintec_project.settings')

application = get_asgi_application()


# Asynchronous Server Gateway Interface
# It is the modern successor of WSGI
# Acts as a bridge between a web Server like Apache or Nginx and your Django application
# It is a standard for Asynchronous web application.
      # Meaning it allows a single process to handle many concurrent connections simultaneously without blocking. This is achieved through an event loop.
# Protocol Support - It is designed for HTTP, WebSockets and HTTP/2 requests.
# Common Servers - Daphne & Uvicorn
# Best for Real-time applications(chats, notifications) high concurrency workloads and long-lived connections.
