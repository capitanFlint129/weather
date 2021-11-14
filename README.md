# Weather statistics

### Установка зависимостей:
```shell
pip install -r requirements.txt
```
### Запуск
#### В контейнере
```shell
docker run -d -e API_KEY='<api key>' -p 8080:8080 --name weather tekkengod129/weather:0.0.1
```
Пример запроса: http://127.0.0.1:8080/weather?city=Moscow&days=3
#### Локально
```shell
export API_KEY=<api key>
export FLASK_APP=app
flask run
```
