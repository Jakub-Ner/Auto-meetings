from flask import Flask

def next():
        with open("../variables/next_meeting.json", "r") as meeting:
            return meeting.read()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "password"
    app.jinja_env.globals.update(next_meeting = next)

    from .website import website

    app.register_blueprint(website, url_prefix="/")

    return app