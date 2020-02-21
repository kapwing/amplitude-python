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

    def create_event(self, **kwargs):
        device_id = kwargs.get('device_id')
        event_type = kwargs.get('event_type')
        user_id = kwargs.get('user_id')

        if not isinstance(event_type, str):
            return None

        if not (isinstance(device_id, str) or isinstance(device_id, str)):
            return None

        event = dict(
            event_type=event_type,
            time=int(time.time() * 1000),
        )

        if device_id:
            event['device_id'] = device_id

        if user_id:
            event['user_id'] = user_id

        for key in ['event_properties', 'user_properties']:
            value = kwargs.get(key)
            if not isinstance(value, dict):
                continue

            event[key] = value

        return event

    def log(self, **kwargs):
        event = self.create_event(**kwargs)
        return self.send_event(event)

    def send_event(self, event):
        if not (self.enabled and event):
            return

        return self.send_events([event])

    def send_events(self, events):
        if not (self.enabled and events):
            return

        return requests.post(
            self.api_url,
            json=dict(api_key=self.api_key, events=events)
        )
