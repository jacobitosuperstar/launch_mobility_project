from flask import (
    Flask,
)
# database
from flask_sqlalchemy import SQLAlchemy
# database migrations
from flask_migrate import Migrate
# hashing the passwords
from flask_bcrypt import Bcrypt
# managin login sessions
from flask_login import LoginManager
# configuration
from .config import (
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
)


app = Flask(__name__)
# configuration object
app.config.from_object(ProductionConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# password encryption
bcrypt = Bcrypt(app)

# login manager
login_manager = LoginManager(app=app)

# importing the routes
# has to be done here, circular imports if done otherwise
from users import views
