import datetime
import json

from flask import Blueprint, jsonify, Response, request

from weather_statistics import weather_api

weather = Blueprint('weather', __name__)


@weather.route('/weather', methods=['GET'])
def get_city_data_for_last_days():
    city = request.args.get('city')
    days = request.args.get('days')
    if not city or not days:
        return Response(
            response='You should set "city" and "days"',
            status=400,
        )
    end_date = datetime.date.today()
    try:
        start_date = (end_date - datetime.timedelta(days=int(days) - 1))
    except ValueError:
        return Response(
            response=json.dumps({
                'days': "must be integer"
            }),
            status=400,
        )

    weather_data = weather_api.get_city_historical_statistics(city, start_date, end_date)
    if weather_data is None:
        return Response(
            response=json.dumps({
                'error': "can't get data"
            }),
            status=500,
        )
    date_fromat = '%Y-%m-%d'
    response_data = {
        "devOpsSchool": "done",
        "city": city,
        "from": start_date.strftime(date_fromat),
        "to": end_date.strftime(date_fromat),
    }
    response_data.update(weather_data)
    return jsonify(response_data)
