"""
ASGI config for hosptalsam project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# import os
#
# from django.core.asgi import get_asgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hosptalsam.settings")
#
# application = get_asgi_application()
import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hosptalsam.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        # Just HTTP for now. (We can add other protocols later.)
    }
)