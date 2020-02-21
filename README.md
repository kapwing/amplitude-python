# amplitude-python

Python API for Amplitude Analytics Logging - https://amplitude.com

This API is a simple (unofficial) wrapper for the [Amplitude HTTP API](https://amplitude.zendesk.com/hc/en-us/articles/204771828-HTTP-API)

## 1. Install amplitude-python

Potential preparation before installing: create and activate virtualenv or conda environment

### 1.1 Install from pypi with conda or pip

```bash
pip install amplitude-python
```

### 1.2 Install from github

```bash
$ git clone https://github.com/kapwing/amplitude-python.git
$ cd amplitude-python
$ pipenv instal
```

## 2. Logging to Amplitude with amplitude-python

Recommend having a look at [Amplitude HTTP API Documentation](https://amplitude.zendesk.com/hc/en-us/articles/204771828-HTTP-API) before start logging.

```python
import amplitude

# initialize amplitude logger
amplitude_logger = amplitude.AmplitudeLogger(api_key='SOME_API_KEY_STRING')

# example event
response = amplitude_logger.log(
    device_id='somedeviceid',
    event_type='justtesting',
    event_properties=dict(property1='somevalue', propertyN='anothervalue')
)

```

## 3. Test amplitude-python module

`python setup.py test`
