# security
Home security system

* Running
/etc/rc.local:

sudo ifconfig eth0 down
sudo macchanger --mac b8:27:eb:f3:23:00 eth0
sudo ifconfig eth0 up

sudo -H -u pi /var/www/security/security_server/manage.py runserver 0.0.0.0:8000
