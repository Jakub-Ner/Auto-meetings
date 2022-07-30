from flask import Flask, redirect

from .website import website
from .jinja_functions import next, delete

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "password"
    app.jinja_env.globals.update(next_meeting = next)
    app.jinja_env.globals.update(delete_meeting = delete)

    app.register_blueprint(website, url_prefix="/")

    return app