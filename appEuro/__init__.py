# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:31:52 2019

@author: Utilisateur
"""
import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler

# new
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from flask_pagedown import PageDown
from config import config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

bcrypt = Bcrypt()
login = LoginManager()
login.login_view = "users.login"


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)

    pagedown.init_app(app)

    # Flask-Login configuration
    from appEuro.models import User

    @login.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from appEuro.recipes import recipes_blueprint
    app.register_blueprint(recipes_blueprint)

    from appEuro.users import users_blueprint
    app.register_blueprint(users_blueprint)
#
#    from .auth import auth as auth_blueprint
#    app.register_blueprint(auth_blueprint, url_prefix='/auth')
#
#    from .api import api as api_blueprint
#    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    return app
