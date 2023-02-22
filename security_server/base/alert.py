import os
import yagmail


class Alert:
    """Alert on compromised security."""

    SENDER = "gvkunchev@gmail.com"
    PASSWORD = os.environ.get('GMAIL_PASS')
    RECIPIENT = "gvkunchev@gmail.com"
    SUBJECT = "Home Security"
    BODY = "Security in your home is compromised!"

    def __init__(self):
        """Initializator."""
        self._yag = yagmail.SMTP(self.SENDER, self.PASSWORD)

    def send_alert(self):
        """Send alert email."""
        self._yag.send(self.TO, self.SUBJECT, self.BODY)
