
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soporte.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
