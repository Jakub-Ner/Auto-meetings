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
from website.jinja_functions import save_meetings, next_meeting

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


import logging


# @buttons.route("/menu", methods=['POST'])
# @base
def menu():
    try:
        if request.form["menu"] == "sign-up":

            subprocess.run(shlex.split(f"/bin/bash {os.getcwd()}/scripts/auth.sh"))
    except Exception as e:
        logging.error(e)
    except BadRequestKeyError:
        ...

    try:
        if request.form["menu"] == "sleep":
            code, next = next_meeting()

            if code != 200:
                sleeping_time = 10 * 60 * 60
            else:
                sleeping_time, _, _, _ = next

            flash(f"Computer will hibernate and wake up after around {sleeping_time} minutes")
            sleeping_thread = Thread(target=sleep, args=(sleeping_time,))
            sleeping_thread.start()

    except BadRequestKeyError:
        ...

    try:
        if "record" in request.form["menu"]:
            record_settings = request.form["menu"] == 'record-on'

            with open("variables/config.json", "r+") as config:
                config = json.load(config)

            config["record"] = record_settings

            with open("variables/config.json", "w+") as config_new:
                json.dump(config, config_new, indent=2)
    except BadRequestKeyError:
        ...


def sleep(sleeping_time):
    time.sleep(7)
    os.system(start_sleep + str(sleeping_time - 1))
