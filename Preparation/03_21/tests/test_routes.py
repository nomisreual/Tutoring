# test_routes.py
from app.models import User


def test_hello(client):
    """
    Test whether the main pages returns the correct content.
    """
    response = client.get("/")
    assert b"Hello!" == response.data


def test_register(client, app):
    """
    Test whether registration works.
    """
    response = client.get("/register/simon")

    # Check whether the registration was a success:
    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().username == "simon"

    # Check the repsonse:
    assert b"Registered!" == response.data


def test_register_check_username(client, app):
    """
    Test whether attempted registration is rejected in case a user
    is already registered with the same username.
    """

    # Register a user:
    client.get("/register/simon")

    response = client.get("/register/simon")
    assert b"Please choose another username" == response.data


def test_users(client):
    # Register the user beforehand:
    client.get("/register/pete")

    response = client.get("/user/pete")
    assert b"Username: pete, password: please_change" == response.data


def test_login_success(client):
    # Register the user beforehand:
    client.get("/register/pete")

    response = client.get("login/pete/please_change")
    assert b"You are now logged in." == response.data


def test_login_wrong_pw(client):
    # Register the user beforehand:
    client.get("/register/pete")

    response = client.get("login/pete/1234")
    assert b"Wrong username, or password." == response.data


def test_login_wrong_user(client):
    # Register the user beforehand:
    client.get("/register/pete")

    response = client.get("login/henry/please_change")
    assert b"Wrong username, or password." == response.data


def test_change_pw_success(client, app):
    # Register the user beforehand:
    client.get("/register/pete")

    response = client.get("/user/pete/please_change/1234")

    with app.app_context():
        assert User.query.first().password == "1234"


def test_change_pw_wrong_credentials(client):
    # Register the user beforehand:
    client.get("/register/pete")

    response = client.get("/user/pete/super_secret/1234")

    assert b"Wrong username, or password." == response.data
