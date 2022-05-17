# user_updater/views.py

from user_updater import app
from .models import User


@app.route("/")
@app.route("/home/")
def hello():
    users = User.query.all()
    user_list = [{
        "id": user.id,
        "firt_name": user.first_name,
        "middle_name": user.middle_name,
        "last_name": user.last_name,
        "email": user.email,
        "zip_code": user.zip_code,
        "city": user.city,
        "county": user.county,
        "state": user.state,
    } for user in users]
    response = {
        "status": 200,
        "users": user_list,
    }
    return response
