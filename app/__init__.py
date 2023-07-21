from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .config import Config
from .auth import auth
from .repositories.user_repository import UserRepository

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return UserRepository.find(user_id)


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    login_manager.init_app(app)

    app.register_blueprint(auth)

    return app
