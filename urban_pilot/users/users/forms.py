# users/forms.py

from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    StringField,
    PasswordField,
    BooleanField,
)
from wtforms.validators import (
    # DataRequired,
    InputRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
    Optional,
    NumberRange,
)
from users.models import User


class RegistrationForm(FlaskForm):
    """User registration Form"""

    # first name
    first_name = StringField(
        label="first_name",
        validators=[
            InputRequired(),
            Length(min=2, max=20),
        ]
    )

    # second name
    middle_name = StringField(
        label="middle_name",
        validators=[
            InputRequired(),
            Length(min=2, max=20),
        ]
    )

    # last name
    last_name = StringField(
        label="last_name",
        validators=[
            InputRequired(),
            Length(min=2, max=20),
        ]
    )

    # email
    email = StringField(
        label="email",
        validators=[
            InputRequired(),
            Email(),
        ]
    )

    # zip code
    zip_code = StringField(
        label="zip_code",
        validators=[
            InputRequired(),
            Length(min=5, max=5),
        ]
    )

    # password
    password = PasswordField(
        label="password",
        validators=[
            InputRequired(),
        ]
    )

    # confirm password
    confirm_password = PasswordField(
        label="confirm_password",
        validators=[
            InputRequired(),
            EqualTo(
                fieldname="password",
                message="The passwords don't match",
            ),
        ]
    )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("The email is already registered")


class UpdateInformationForm(FlaskForm):
    """User information updater Form"""
    # user id
    user_id = IntegerField(
        label="user_id",
        validators=[
            InputRequired(),
            NumberRange(
                min=1,
                message="El valor del ID debe ser de 1 en adelante",
            )
        ]
    )

    # first name
    first_name = StringField(
        label="first_name",
        validators=[
            Optional(),
            Length(
                min=2,
                max=20
            ),
        ]
    )

    # second name
    middle_name = StringField(
        label="middle_name",
        validators=[
            Optional(),
            Length(
                min=2,
                max=20
            ),
        ]
    )

    # last name
    last_name = StringField(
        label="last_name",
        validators=[
            Optional(),
            Length(
                min=2,
                max=20
            ),
        ]
    )

    # email
    email = StringField(
        label="email",
        validators=[
            Optional(),
            Email(),
        ]
    )

    # zip code
    zip_code = StringField(
        label="zip_code",
        validators=[
            Optional(),
            Length(
                min=5,
                max=5
            ),
        ]
    )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("The email is already registered")


class DeletionForm(FlaskForm):
    """User deleter Form"""
    # user id
    user_id = IntegerField(
        label="user_id",
        validators=[
            InputRequired(),
        ]
    )


class LoginForm(FlaskForm):
    """Formulario de logueo."""
    # email
    email = StringField(
        label="email",
        validators=[
            InputRequired(),
            Email(),
        ]
    )

    # password
    password = PasswordField(
        label="password",
        validators=[
            InputRequired(),
        ]
    )

    # remember me
    remember_me = BooleanField(
        label="remember_me",
    )
