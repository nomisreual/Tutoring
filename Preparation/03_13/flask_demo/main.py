from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), index=True,
                                          unique=True)
    password: Mapped[str] = mapped_column(String(64))

    def set_password(self, password: str) -> None:
        self.password = password

    def check_password(self, password: str) -> bool:
        return self.password == password


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


@app.route("/login/<usr>")
def login(usr: str):
    # logic
    return "You are now logged in."


@app.route("/user/<usr>/<old_pw>/<new_pw>")
def change_pw(usr: str, old_pw: str, new_pw: str):
    # logic
    return f"{usr}, your password has been updated"


if __name__ == "__main__":
    app.run()
