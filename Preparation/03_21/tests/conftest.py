import pytest

from app import create_app, db
from app.models import User


@pytest.fixture()
def app():
    app = create_app("sqlite://")
    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
