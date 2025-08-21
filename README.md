# Home security server

* Requires
  - a virutalenv with
    - requirements.txt installed
    - env variables for Django secret key (DJANGO_SECRET_KEY), password pattern (UNLOCK_PATTERN), gmail password for the user (GMAIL_PASS)
        * use app password, not your real password - https://myaccount.google.com/apppasswords

* Database preparation
  The first start requires a prepared database objects:
  ```
  manage.py shell
  > from base.models import ArmStatus
  > ArmStatus.objects.create()
  > from base.models import Sensor
  > Sensor.objects.create(location=, pin_in=, pin_out=, state=Sensor.Status.CLOSED)
  """
  My pins:
    Sensor.objects.create(location="Bed room", pin_in=37, pin_out=36, state=Sensor.Status.CLOSED)
    Sensor.objects.create(location="Kid room", pin_in=40, pin_out=38, state=Sensor.Status.CLOSED)
    Sensor.objects.create(location="Front door", pin_in=35, pin_out=33, state=Sensor.Status.CLOSED)
  """
  ```

* Running
  vim /etc/rc.local:
    ```
    # The lines below are just for my personal Pi - I have mac binding in my ISP's hardware
    sudo ifconfig eth0 down
    sudo macchanger --mac b8:27:eb:f3:23:00 eth0
    sudo ifconfig eth0 up

    sudo -H -u pi /var/www/security/start
    ```

* Known issues
  - The API should be behind API token to ensure authorized access.
    The poor Pi cannot handle this, though. It takes 2-3 seconds to verify the token.
    As a workaround - the API is locked to 192.168.100.50, meaning it can only be accessed from within the local network.

    A way to hack it:
    - Go to the front door;
    - Hack the Wifi password;
    - Bruteforce the server password;
    - Disable the security from within the server itself.

    Probably requires too much time. Also, if there is no electricity, there is no home security either. So this is App is not going to be super secure EVER!
