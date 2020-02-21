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
    def __init__(self, api_key, api_url=DEFAULT_API_URL):
        self.api_key = api_key
        self.api_url = api_url
        self.enabled = True

    def prepare_event(self, **event):
        if not event.get('event_type'):
            raise ValueError('Missing event type')

        if not (event.get('device_id') or event.get('user_id')):
            raise ValueError('Missing both device & user Ids, at least one must be provided')

        event.setdefault('time', int(time.time() * 1000))

        return event

    def log(self, **kwargs):
        options = kwargs.pop('options', None)

        event = self.prepare_event(**kwargs)
        return self.send_event(event, options=options)

    def send_event(self, event, options=None):
        if not (self.enabled and event):
            return

        return self.send_events([event], options=options)

    def send_events(self, events, options=None):
        if not (self.enabled and events):
            return

        return requests.post(
            self.api_url,
            json=dict(api_key=self.api_key, events=events, options=options)
        )
