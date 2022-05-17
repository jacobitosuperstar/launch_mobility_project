# users/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration"""
    SECRET_KEY = "3fe63dc80e8eb87d493a92b3eaed7d87fb1976c2e0757315d6"
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = (
        'sqlite:///' + os.path.join(basedir, 'urban_pilot_users.sqlite')
    )
    # SQLALCHEMY_BINDS = {
    #     "users": (
    #         "sqlite:///" + os.path.join(basedir, "urban_pilot_users.sqlite")
    #     )
    # }


class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = (
        'sqlite:///' + os.path.join(basedir, 'urban_pilot_users.sqlite')
    )
    # SQLALCHEMY_BINDS = {
    #     "users": (
    #         "sqlite:///" + os.path.join(basedir, "urban_pilot_users.sqlite")
    #     )
    # }


class ProductionConfig(BaseConfig):
    """Production configuration."""
    # SECRET_KEY = "3fe63dc80e8eb87d493a92b3eaed7d87fb1976c2e0757315d6"
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DB_USER = "jacobo"
    DB_PASSWORD = "mateo"
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@db:5432/urban_pilot_users"
    )
    # SQLALCHEMY_BINDS = {
    #     "users": (
    #         f"postgresql://{DB_USER}:{DB_PASSWORD}@db:5432/urban_pilot_users",
    #     )
    # }
