from flask import Flask

from .website import website
from .jinja_functions import next

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "password"
    app.jinja_env.globals.update(next_meeting = next)

    app.register_blueprint(website, url_prefix="/")

    return app