from .models import Sensor, ArmStatus
from threading import Timer


class Armer:
    """Monitor for intruders."""

    TIME_DELTA = 0.3 # Delay between checks on the sensors and doors
    TIMEOUT = 30 # Time during which the user must to enter the pattern

    def __init__(self):
        """Initialize."""
        self._sensors = Sensor.objects.all()
        self._arm_status = ArmStatus.objects.all().first()
        self._monitor_status()
    
    def _check_verification(self):
        """Ensure that the home is verified after opening the door."""
        if self._arm_status == ArmStatus.Status.DISARMING:
            self._arm_status = ArmStatus.Status.COMPROMISED

    def _monitor_status(self):
        """Monitor sensor and arm status."""
        if self._arm_status == ArmStatus.Status.ARMED:
            for sensor in self._sensors:
                if sensor.state == Sensor.Status.OPEN:
                    sensor.state = Sensor.Status.DISARMING
                    Timer(self.TIMEOUT, self._check_verification).start()
        Timer(self.TIME_DELTA, self._monitor_status).start()
