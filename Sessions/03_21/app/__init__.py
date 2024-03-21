# Import Flask:
from flask import Flask

from .models import User, db


def create_app(database_uri="sqlite:///app.db"):
    # Create a flask application and set the database URI:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

    # Initialize the database:
    db.init_app(app)

    # Routes:
    @app.route("/")
    def hello():
        db.drop_all()
        db.create_all()
        return "Hello!"

    @app.route("/register/<usr>")
    def register(usr: str):
        # Check for registered user with same username:
        check = User.query.filter_by(username=usr).first()
        if check:
            return "Please choose another username."
        user = User(username=usr, password="please_change")
        db.session.add(user)
        db.session.commit()
        return "Registered!"

    @app.route("/user/<usr>")
    def users(usr: str):
        user = User.query.filter_by(username=usr).first()
        return f"Username: {user.username}, password: {user.password}"

    @app.route("/login/<usr>/<passwd>")
    def login(usr: str, passwd: str):
        user: User = User.query.filter_by(username=usr).first()
        if user and user.check_password(passwd):
            return "You are now logged in."
        return "Wrong username, or password."

    @app.route("/user/<usr>/<old_pw>/<new_pw>")
    def change_pw(usr: str, old_pw: str, new_pw: str):
        user: User = User.query.filter_by(username=usr).first()
        if user and user.check_password(old_pw):
            user.set_password(new_pw)
            db.session.commit()
            return f"{usr}, your password has been updated"
        return "Wrong username, or password."

    return app
