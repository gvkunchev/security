import logging
from threading import Timer

from .models import Sensor, ArmStatus
from .alert import Alert


logger = logging.getLogger('default_logger')


class Armer:
    """Monitor for intruders."""

    TIME_DELTA = 0.3 # Delay between checks on the sensors and doors
    TIMEOUT = 30 # Time during which the user must to enter the pattern

    def __init__(self):
        """Initialize."""
        self._sensors = Sensor.objects.all()
        self._arm_status = ArmStatus.objects.all().first()
        self._alert = Alert()
        self._monitor_status()
    
    def _check_verification(self):
        """Ensure that the home is verified after opening the door."""
        self._arm_status.refresh_from_db()
        if self._arm_status.state == ArmStatus.Status.DISARMING:
            logger.error('Setting compromised status.')
            self._arm_status.state = ArmStatus.Status.COMPROMISED
            self._arm_status.save()
            self._alert.send_alert()

    def _monitor_status(self):
        """Monitor sensor and arm status."""
        self._arm_status.refresh_from_db()
        if self._arm_status.state == ArmStatus.Status.ARMED:
            for sensor in self._sensors:
                sensor.refresh_from_db()
                if sensor.state == Sensor.Status.OPEN:
                    logger.warning(f'Open door detected: {sensor.location}')
                    self._arm_status.state = ArmStatus.Status.DISARMING
                    self._arm_status.save()
                    logger.info('Setting disarming status.')
                    Timer(self.TIMEOUT, self._check_verification).start()
                    break
        Timer(self.TIME_DELTA, self._monitor_status).start()
