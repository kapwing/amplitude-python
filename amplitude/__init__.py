import requests
import time
import json

# Documentation of AmplitudeHTTP API:
#   https://amplitude.zendesk.com/hc/en-us/articles/204771828
#
# Convert Curl queries - such as below to - python:
#   https://curl.trillworks.com/
#
# Example HTTP Curl Query for Amplitude:
#   curl --data 'api_key=SOMEIDOFAKIND' --data 'event=[{'user_id':'john_doe@gmail.com', 'event_type':'watch_tutorial', 'user_properties':{'Cohort':'Test A'}, 'country':'United States', 'ip':'127.0.0.1', 'time':1396381378123}]' https://api.amplitude.com/httpapi

DEFAULT_API_URL = 'https://api.amplitude.com/2/httpapi'

class AmplitudeLogger:
    def __init__(self, api_key, api_uri=DEFAULT_API_URL):
        self.api_key = api_key
        self.api_uri = api_uri
        self.enabled = True

    def _is_none_or_not_str(self, value):
        return value is None or type(value) is not str

    def create_event(self, **kwargs):
        event = dict()

        device_id = kwargs.get('device_id', None)
        event_type = kwargs.get('event_type', None)
        user_id = kwargs.get('user_id', None)

        if self._is_none_or_not_str(event_type):
            return None

        if self._is_none_or_not_str(user_id) and self._is_none_or_not_str(device_id):
            return None

        event['event_type'] = event_type
        event['time'] = int(time.time() * 1000)

        if device_id:
            event['device_id'] = device_id

        if user_id:
            event['user_id'] = user_id

        user_properties = kwargs.get('user_properties', None)
        if isinstance(user_properties, dict):
            event['user_properties'] = user_properties

        event_properties = kwargs.get('event_properties', None)
        if isinstance(event_properties, dict):
            event['event_properties'] = event_properties

        return event

    def log(self, **kwargs):
        event = self.create_event(**kwargs)
        self.send_event(event)

    def send_event(self, event):
        if not (self.enabled and event):
            return

        return self.send_events([event])

    def send_events(self, events):
        if not (self.enabled and event):
            return

        return requests.post(
            self.api_uri,
            json=dict(api_key=self.api_key, events=events)
        )
