from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    from . import models
    return app