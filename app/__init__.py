# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# after existing third-party imports
from flask_login import LoginManager

# after existing third-party imports
from flask_bootstrap import Bootstrap
# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
# after the db variable initialization
login_manager = LoginManager()





def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)

    Bootstrap(app)


    from app import models



    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .SurveyForms import SurveyForms as SurveyForms_blueprint
    app.register_blueprint(SurveyForms_blueprint)




    return app
