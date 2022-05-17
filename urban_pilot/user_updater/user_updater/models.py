# user_updater/models.py

from user_updater import db


class User(db.Model):
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
        default="00000",
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

    def __repr__(self):
        return f"User: {self.email}"
