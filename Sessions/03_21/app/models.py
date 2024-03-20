# Import ORM tooling:
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

# Create a database object:
db = SQLAlchemy()


# Declare a database table:
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    password: Mapped[str] = mapped_column(String(64))

    def set_password(self, password: str) -> None:
        self.password = password

    def check_password(self, password: str) -> bool:
        return self.password == password
