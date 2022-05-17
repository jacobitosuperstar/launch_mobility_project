# user_updater/__init__.py

from flask import Flask
# database
from flask_sqlalchemy import SQLAlchemy
# database migrations
from flask_migrate import Migrate
# configuration
from user_updater.config import (
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
)


app = Flask(__name__)
# configuration object
app.config.from_object(ProductionConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# views
from user_updater import views
