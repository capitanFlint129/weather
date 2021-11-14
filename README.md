# Weather statistics

Сервис развернут по адресу: weather.p5.do-school.ru

#### GET /weather?city={city name}&days={number of days}
Пример ответа:

```json
{
  "city": "Moscow",
  "from": "2021-11-12",
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
  "to": "2021-11-14"
}
```

## Локальная разработка
### Установка зависимостей:
```shell
pip install -r requirements.txt
```
### Запуск
Пример запроса: http://127.0.0.1:8080/weather?city=Moscow&days=3
#### В контейнере
```shell script
docker run -d -e API_KEY='<api key>' -p 8080:8080 --name weather tekkengod129/weather:latest
```
#### Локально
```shell script
export API_KEY=<api key>
export FLASK_APP=main
flask run
```

Можно использовать gunicorn
```shell script
gunicorn -w 2 main:app -b 0.0.0.0:8080
```
