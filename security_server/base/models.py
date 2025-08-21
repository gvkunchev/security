from datetime import datetime
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

    def __str__(self):
        return self.location


class ArmStatus(models.Model):
    """Armed/unarmed security status."""

    class Status(models.TextChoices):
        """Arm status state representation."""
        ARMED = 'Armed'
        UNARMED = 'Unarmed'
        DISARMING = 'Disarming'
        COMPROMISED = 'Compromised'

    location = models.CharField(max_length=100)
    state = models.CharField(max_length=20,
                             choices=Status.choices,
                             default=Status.UNARMED)
    last_armed_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.location
