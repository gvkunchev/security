from .models import Sensor
import RPi.GPIO as GPIO
from threading import Timer


class Sensors:
    """Monitoring for all sensors."""
    HISTORY_LENGTH = 5 # Number of results to be stored to get average results
    TIME_DELTA = 0.15 # Delay between checks on the input

    def __init__(self):
        """Initialize."""
        self._sensors = Sensor.objects.all()
        self._history = []
        self._init_board()
        self._init_sensors()
        self._monitor_status()
    
    def _init_board(self):
        """Initialize the Pi board."""
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
    
    def _init_sensors(self):
        """initialize sensors."""
        for sensor in self._sensors:
            self._history.append([0] * self.HISTORY_LENGTH)
            GPIO.setup(sensor.pin_out, GPIO.OUT)
            GPIO.output(sensor.pin_out, GPIO.HIGH)
            GPIO.setup(sensor.pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    def _monitor_status(self):
        """Monitor sensor status."""
        for sensor, history in zip(self._sensors, self._history):
            history.pop(0)
            history.append(GPIO.input(sensor.pin_in))
            if history.count(0) == 0:
                sensor.state = Sensor.Status.CLOSED
            else:
                sensor.state = Sensor.Status.OPEN
            sensor.save()
        Timer(self.TIME_DELTA, self._monitor_status).start()
