
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from protocol.config import Config
from flask_admin import Admin
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)



admin = Admin()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        db.init_app(app)

    login_manager.init_app(app)

    from protocol.routes import MyAdminIndexView

    admin.init_app(app, index_view=MyAdminIndexView())

    from protocol.routes import main
    app.register_blueprint(main)

    return app
