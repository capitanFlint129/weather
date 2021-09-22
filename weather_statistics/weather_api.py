import os

import numpy as np
import requests


API_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata'
API_DATE_FORMAT = '%Y-%m-%d'
REGION = 'RU'


def get_city_historical_statistics(city, start_date, end_date):
    url = API_URL + f'/history'
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
