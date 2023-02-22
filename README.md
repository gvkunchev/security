# security
Home security system

* Running
/etc/rc.local:

sudo ifconfig eth0 down
sudo macchanger --mac b8:27:eb:f3:23:00 eth0
sudo ifconfig eth0 up

sudo -H -u pi /var/www/security/start

* Known issues
The API should be behind API token to ensure authorized access.
The poor Pi cannot handle this, though. It takes 2-3 seconds to verify the token.
As a workaround - the API is locked to 192.168.100.50, meaning it can only be accessed from within the local network.

A way to hack it:
- Go to the front door;
- Hack the Wifi password;
- Bruteforce the server password;
- Disable the security from within the server itself.

Probably requires too much time. Also, if there is no electricity, there is no home security either. So this is App is not going to be super secure EVER!
