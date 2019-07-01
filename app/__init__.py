import os

from flask import Flask
from peewee import DoesNotExist
from jinja2.exceptions import TemplateNotFound
from app.admin import admin as admin_blueprint
from app.extensions import db
from app.main.views import main as main_blueprint
from app.utils import not_exist
from configs import config


def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "development")
    app.config.from_object(config[env])
    db.init_app(app)
    app.register_error_handler(DoesNotExist, not_exist)
    app.register_error_handler(TemplateNotFound, not_exist)
    app.register_error_handler(404, not_exist)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint)
    return app
