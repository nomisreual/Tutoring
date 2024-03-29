# Import Flask:
from flask import Flask
# Import ORM tooling:
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

# Create a flask application and set the database URI:
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
# Create a database object:
db = SQLAlchemy(app)


# Declare a database table:
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), index=True,
                                          unique=True)
    password: Mapped[str] = mapped_column(String(64))

    def set_password(self, password: str) -> None:
        self.password = password

    def check_password(self, password: str) -> bool:
        return self.password == password


# Routes:

@app.route("/")
def hello():
    db.drop_all()
    db.create_all()
    return "Hello!"


@app.route("/register/<usr>")
def register(usr: str):
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
    return "Wrong username, or password"


# Run the app when this file is executed.
if __name__ == "__main__":
    app.run()
