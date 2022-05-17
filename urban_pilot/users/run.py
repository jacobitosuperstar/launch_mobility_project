from users import app
from users import db


if __name__ == '__main__':
    db.create_all()
    app.run(
        host='0.0.0.0',
        port='8000',
        debug=True,
        threaded=True
    )
