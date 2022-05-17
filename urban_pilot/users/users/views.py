# users/views.py

import json
from users import (
    app,
    bcrypt,
    db,
)
from flask import (
    request,
    # redirect, url_for,
)
from .forms import (
    RegistrationForm,
    UpdateInformationForm,
    DeletionForm,
    LoginForm,
)
from .models import (
    User,
)
from .producer import (
    rabbit_mq_sender,
)
# data structure of the form data when senden in the request
from werkzeug.datastructures import ImmutableMultiDict
# login??
from flask_login import (
    login_user,
    logout_user,
)


@app.route(rule="/", methods=["GET"])
@app.route(rule="/home/", methods=["GET"])
def home():
    """Página de llegada."""
    response = {
        "status": 200,
        "message": "Hola Mundo"
    }
    return response


@app.route(rule="/register/", methods=["POST"])
def registration():
    """User regristration endpoint."""
    values = request.get_json()
    values = json.loads(values)
    values = ImmutableMultiDict(values)
    form = RegistrationForm(values)
    if form.validate():
        # generating the hashed password
        hashed_password = bcrypt.generate_password_hash(
            password=form.password.data,
            rounds=12,
        ).decode(encoding="utf-8")
        # creating the new user instance
        user = User(
            first_name=form.first_name.data,
            middle_name=form.middle_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            zip_code=form.zip_code.data,
            password=hashed_password,
        )
        # saving the user in the db
        db.session.add(user)
        db.session.commit()
        response = {
            "status": 200,
            "message": "Account created successfully",
            "user": {
                "id": user.id,
                "firt_name": user.first_name,
                "middle_name": user.middle_name,
                "last_name": user.last_name,
                "email": user.email,
                "zip_code": user.zip_code,
            },
        }
        rabbit_mq_sender(
            message=response,
            host="rabbitmq",
            port="5672",
            queue_name="user_updater",
            routing_key="user.information.updater",
            exchange="information.updater",
        )
        rabbit_mq_sender(
            message={"zip_code": user.zip_code, "operation": "add"},
            host="rabbitmq",
            port="5672",
            queue_name="location_tracker",
            routing_key="user.location.tracker",
            exchange="location.tracker",
        )
    else:
        response = {
            "status": 403,
            "message": "We couldn't validate the form values",
            "errors": form.errors,
        }
    return response


@app.route(rule="/updater/", methods=["POST"])
def updater():
    """User regristration endpoint."""
    values = request.get_json()
    values = json.loads(values)
    values = ImmutableMultiDict(values)
    form = UpdateInformationForm(values)
    if form.validate():
        # get user instance
        user_id = form.user_id.data
        user = User.query.filter_by(id=user_id).first()
        # getting the data
        first_name = form.first_name.data
        middle_name = form.middle_name.data
        last_name = form.last_name.data
        email = form.email.data
        zip_code = form.zip_code.data
        # update user instance
        if first_name:
            user.first_name = first_name
        if middle_name:
            user.middle_name = middle_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email
        if zip_code:
            rabbit_mq_sender(
                message={"zip_code": user.zip_code, "operation": "substract"},
                host="rabbitmq",
                port="5672",
                queue_name="location_tracker",
                routing_key="user.location.tracker",
                exchange="location.tracker",
            )
            user.zip_code = zip_code
        # saving the user in the db
        db.session.add(user)
        db.session.commit()
        response = {
            "status": 200,
            "message": "Account Updated Successfully",
            "user": {
                "id": user.id,
                "firt_name": user.first_name,
                "middle_name": user.middle_name,
                "last_name": user.last_name,
                "email": user.email,
                "zip_code": user.zip_code,
            },
        }
        rabbit_mq_sender(
            message=response,
            host="rabbitmq",
            port="5672",
            queue_name="user_updater",
            routing_key="user.information.updater",
            exchange="information.updater",
        )
        rabbit_mq_sender(
            message={"zip_code": zip_code, "operation": "add"},
            host="rabbitmq",
            port="5672",
            queue_name="location_tracker",
            routing_key="user.location.tracker",
            exchange="location.tracker",
        )
    else:
        response = {
            "status": 403,
            "message": "We couldn't validate the form values",
            "errors": form.errors,
        }
    return response


@app.route(rule="/deleter/", methods=["POST"])
def deleter():
    """User delition endpoint."""
    values = request.get_json()
    values = json.loads(values)
    values = ImmutableMultiDict(values)
    form = DeletionForm(values)
    if form.validate():
        # get user instance
        user_id = form.user_id.data
        user = User.query.filter_by(id=user_id).first()
        # sending the delete message
        rabbit_mq_sender(
            message={"zip_code": user.zip_code, "operation": "substract"},
            host="rabbitmq",
            port="5672",
            queue_name="location_tracker",
            routing_key="user.location.tracker",
            exchange="location.tracker",
        )
        # deleting the user from the db
        db.session.delete(user)
        db.session.commit()
        response = {
            "status": 200,
            "message": "Account deleted successfully",
        }
    else:
        response = {
            "status": 403,
            "message": "We couldn't validate the form values",
            "errors": form.errors,
        }
    return response


@app.route(rule="/login/", methods=["POST"])
def log_in():
    """User login endpoint."""
    values = request.get_json()
    values = json.loads(values)
    values = ImmutableMultiDict(values)
    form = LoginForm(values)
    if form.validate():
        email = form.email.data
        password = form.password.data
        remember_me = form.remember_me.data
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=remember_me)
            # check if the url actually changes
            # return redirect(location=url_for(home), code=302)
            response = {
                "status": 200,
                "message": "Welcome Back"
            }
        else:
            response = {
                "status": 403,
                "message": "The information given is not correct"
            }
    else:
        response = {
            "status": 403,
            "message": "We couldn't validate the form values",
            "errors": form.errors,
        }
    return response


@app.route(rule="/logout/")
def log_out():
    """Logout view."""
    logout_user()
    response = {
        "status": 200,
        "message": "Come back soon"
    }
    return response
