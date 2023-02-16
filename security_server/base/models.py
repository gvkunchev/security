from django.db import models


class Sensor(models.Model):
    """Door sensor representation."""

    class Status(models.TextChoices):
        """Door sensor state representation."""
        OPEN = 'Open'
        CLOSED = 'Closed'
        
    location = models.CharField(max_length=100)
    pin_out = models.IntegerField()
    pin_in = models.IntegerField()
    state = models.CharField(max_length=20,
                             choices=Status.choices,
                             default=Status.OPEN)

