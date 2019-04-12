from flask import (
    Blueprint,
)
from jinja2.exceptions import TemplateNotFound

from app.utils import not_exist
from .health_identify import HealthIdentify

main = Blueprint("main", __name__)
main.register_error_handler(TemplateNotFound, not_exist)
main.add_url_rule("/health", view_func=HealthIdentify.as_view(name="health"), methods=["GET"])
