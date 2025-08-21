import sys

from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        """Create the singletons that monitor the status."""
        if not 'manage.py' in sys.argv:
            from base.sensors import Sensors
            from base.armer import Armer
            # This code is not executed during migrations
            Sensors()
            Armer()
