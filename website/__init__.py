from flask import Flask, render_template

from .website import website
from .buttons import buttons
from .jinja_functions import next, base, get_config


def create_app():
    app = Flask(__name__)

    @app.errorhandler(405)
    @base
    def page_not_found(meetings, e):
        return render_template("base.html", meetings=meetings), 202

    app.config['SECRET_KEY'] = "password"
    app.jinja_env.globals.update(next_meeting=next)
    app.jinja_env.globals.update(get_config=get_config)

    app.register_blueprint(website, url_prefix="/")
    app.register_blueprint(buttons, url_prefix="/")

    return app
