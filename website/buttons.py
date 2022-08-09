import os
import time

from flask import Blueprint, request
from flask.helpers import flash
from werkzeug.exceptions import BadRequestKeyError
from threading import Thread
import json
import shlex
import subprocess

from variables.operating_systems.Ubuntu import start_sleep
from website.jinja_functions import save_meetings, next_meeting, path_to_variables

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
def menu():
    try:
        if request.form["menu"] == "sign-up":
            try:
                subprocess.call(shlex.split("sudo ./auth.sh"))
            except Exception as e:
                print(e)
    except BadRequestKeyError:
        ...

    try:
        if request.form["menu"] == "sleep":
            sleeping_time, _, _, _ = next_meeting()

            flash(f"Computer will hibernate and wake up after around {sleeping_time} minutes")
            sleeping_thread = Thread(target=sleep, args=(sleeping_time,))
            sleeping_thread.start()

    except BadRequestKeyError:
        ...

    try:
        if "record" in request.form["menu"]:
            record_settings = request.form["menu"] == 'record-on'

            with open(path_to_variables + "/config.json", "r+") as config:
                config = json.load(config)

            config["record"] = record_settings

            with open(path_to_variables + "/config.json", "w+") as config_new:
                config_new.write(json.dumps(config))
    except BadRequestKeyError:
        ...


def sleep(sleeping_time):
    time.sleep(7)
    os.system(start_sleep[0] + str(sleeping_time - 1) + start_sleep[1])
