from flask import Blueprint, request, flash
from werkzeug.exceptions import BadRequestKeyError
import json
import shlex
import subprocess

from website.jinja_functions import save_meetings

buttons = Blueprint("buttons", __name__)


# @buttons.route("/delete", methods=['POST'])
# @base
def delete(meetings):
    try:
        meetings.pop(request.form["delete"])
        save_meetings(meetings)
        flash("Meeting deleted", category="success")

    except BadRequestKeyError:
        ...


# @buttons.route("/menu", methods=['POST'])
# @base
def menu(meetings):
    try:
        if request.form["menu"] == "sign-up":
            try:
                subprocess.call(shlex.split("./auth.sh"))
            except Exception as e:
                print(e)
    except BadRequestKeyError:
        ...

    try:
        if request.form["menu"] == "sleep":
            print("spać")
    except BadRequestKeyError:
        ...

    try:
        if "record" in request.form["menu"]:
            record_settings = request.form["menu"] == 'record-on'

            with open("variables/config.json", "r+") as config:
                config = json.load(config)

            config["record"] = record_settings

            with open("variables/config.json", "w+") as config_new:
                config_new.write(json.dumps(config))
    except BadRequestKeyError:
        ...
