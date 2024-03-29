import os

import pytest

from app import create_app
from app.extensions import db


def pytest_sessionstart(session):
    os.environ["FLASK_ENV"] = "testing"
    create_app()


@pytest.fixture(scope="session")
def app():
    os.environ["FLASK_ENV"] = "testing"
    app = create_app()
    with app.app_context():
        db.database.create_tables([])
        yield app
        db.database.drop_tables([])


@pytest.fixture
def client(app):
    client = app.test_client()
    return client
