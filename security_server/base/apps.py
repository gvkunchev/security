import sys

from django.apps import AppConfig

from base.sensors import Sensors
from base.armer import Armer


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        """Create the singletons that monitor the status."""
        if not 'manage.py' in sys.argv:
            # This code is not executed during migrations
            Sensors()
            Armer()
