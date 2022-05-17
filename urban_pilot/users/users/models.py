# users/models.py

from users import (
    db,
    login_manager,
)
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """Class that contains the user information."""

    # bind key for multiple databases
    # __bind_key__ = "users"

    # table name
    __tablename__ = "users"

    # primary key
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # fist name
    first_name = db.Column(
        db.String(20),
        nullable=False,
    )

    # middle name
    middle_name = db.Column(
        db.String(20),
        nullable=False,
    )

    # last name
    last_name = db.Column(
        db.String(20),
        nullable=False,
    )

    # email
    email = db.Column(
        db.String(120),
        nullable=False,
        unique=True,
    )

    # zip code
    zip_code = db.Column(
        db.String(5),
        nullable=False,
        default='00000',
    )

    # city
    city = db.Column(
        db.String(100),
        nullable=True,
    )

    # county
    county = db.Column(
        db.String(100),
        nullable=True,
    )

    # state
    state = db.Column(
        db.String(100),
        nullable=True,
    )

    # password
    password = db.Column(
        db.String(256),
        nullable=False,
    )

    def __init__(
        self,
        first_name: str,
        middle_name: str,
        last_name: str,
        email: str,
        zip_code: str,
        password: str,
    ):
        self.first_name = first_name[:20]
        self.middle_name = middle_name[:20]
        self.last_name = last_name[:20]
        self.email = email[:120]
        self.zip_code = zip_code[:5]
        self.password = password[:256]

    def __repr__(self):
        return f"User: {self.email}"
