# Weather statistics

## API

Сервис развернут по адресу: weather.p5.do-school.ru

#### GET /weather?city=<str>

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
