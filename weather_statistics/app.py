from flask import Flask

from weather_statistics.handlers import weather


def create_app():
    app = Flask(__name__)
    app.register_blueprint(weather)
    return app
