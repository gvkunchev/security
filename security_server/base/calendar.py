"""Google calendar."""

import logging
import os
import pathlib
import datetime


from google.oauth2 import service_account
from googleapiclient.discovery import build


logger = logging.getLogger('default_logger')


class Calendar:
    """Google calendar."""

    SERVICE_ACCOUNT_FILE = os.path.join(pathlib.Path(__file__).parent.resolve(),
                                        'home-security-469807-88f593cf213c.json')
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    CALENDAR_ID = 'family16050726343873179487@group.calendar.google.com'
    MAX_RESULTS = 10
    EVENTS_KEY = "events"
    TIME_KEY = "time"
    SUMMARY_KEY = "summary"


    def __init__(self):
        """Initializator."""
        self._creds = service_account.Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE,
                                                                            scopes=self.SCOPES)
        self._service = build('calendar', 'v3', credentials=self._creds)

    def get_events(self):
        """Return json of the events."""
        try:
            now = datetime.datetime.now().isoformat() + 'Z'
            events_result = self._service.events().list(
                calendarId=self.CALENDAR_ID,
                timeMin=now,
                maxResults=self.MAX_RESULTS,
                singleEvents=True,
                orderBy='startTime'
            ).execute()
            events = events_result.get('items', [])
            event_list = []
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                event_list.append({self.TIME_KEY: start, self.SUMMARY_KEY: event["summary"]})
            return {self.EVENTS_KEY: event_list}
        except Exception as e:
            logger.error("Error getting calendar events: ", e)
            return {self.EVENTS_KEY: []}


calendar = Calendar()
