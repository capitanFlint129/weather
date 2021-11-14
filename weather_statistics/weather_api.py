import os

import numpy as np
import requests


API_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata'
API_DATE_FORMAT = '%Y-%m-%d'
REGION = 'RU'

MOCKED_TEST_DATA = {
    "humidity": {
        "average": 88.13,
        "max": 89.75,
        "median": 87.65,
        "min": 86.99
    },
    "pressure_mb": {
        "average": 1017.7666666666668,
        "max": 1027.8,
        "median": 1018.5,
        "min": 1007.0
    },
    "temperature_c": {
        "average": 2.1666666666666665,
        "max": 3.2,
        "median": 1.9,
        "min": 1.4
    },
}

def get_city_historical_statistics(city, start_date, end_date):
    url = API_URL + f'/history'
    if os.environ.get('MOCK_WEATHER_API_FOR_TESTS', '0') == '1':
        return MOCKED_TEST_DATA
    response = requests.get(url, params={
        'startDateTime': f'{start_date.strftime(API_DATE_FORMAT)}T00:00:00',
        'endDateTime': f'{end_date.strftime(API_DATE_FORMAT)}T00:00:00',
        'location': f'{city}, {REGION}',
        'unitGroup': 'metric',
        'key': os.environ['API_KEY'],
        'contentType': 'json',
        'aggregateHours': 24,
        'dayStartTime': '0:0:00',
        'dayEndTime': '0:0:00',
    })
    if response.status_code != 200:
        return None
    weather_data = response.json()
    try:
        _, weather_data = weather_data['locations'].popitem()
        weather_data = weather_data['values']
        temperature = np.array([day_data['temp'] for day_data in weather_data])
        humidity = np.array([day_data['humidity'] for day_data in weather_data])
        pressure = np.array([day_data['sealevelpressure'] for day_data in weather_data])
        historical_statistics = {
            "temperature_c": get_statistics(temperature),
            "humidity": get_statistics(humidity),
            "pressure_mb": get_statistics(pressure),
        }
    except KeyError:
        historical_statistics = None

    return historical_statistics


def get_statistics(data):
    return {
        "average": np.average(data),
        "median": np.median(data),
        "min": np.min(data),
        "max": np.max(data),
    }
