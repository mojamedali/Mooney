from flask import Flask
from app.core.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    return app