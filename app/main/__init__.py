from flask import (
    Blueprint,
)

from .health_identify import HealthIdentify

main = Blueprint("main", __name__)
main.add_url_rule("/health", view_func=HealthIdentify.as_view(name="health"), methods=["GET"])
