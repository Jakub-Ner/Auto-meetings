import logging

from flask import render_template
from datetime import datetime
import json
import os

from browser.Meetings import Meetings
from variables.config import config


def base(func):
    with open("variables/meetings.json", "r") as file:
        meetings = Meetings.from_json(json.load(file))

    def website(*args, **kwargs):
        func(meetings, *args, **kwargs)

        new_meetings_json = meetings.to_list()
        return render_template("base.html", meetings=new_meetings_json), 200

    website.__name__ = func.__name__
    return website


def save_meetings(meetings: Meetings):
    try:
        logging.debug("saving meetings:")
        with open("variables/meetings.json", "w") as file:
            json.dump(meetings.to_json(), file)
    except Exception as e:
        logging.error(f"Cannot save meetings: {e}")


def next_meeting():
    meetings_path = "variables/meetings.json"

    # if file is empty give necessary datax
    # with open(meetings_path, "w+") as file:
    #     if os.stat(meetings_path).st_size == 0:
    #         json.dump({}, file)

    with open(meetings_path, "r") as file:
        meeting_json = json.load(file)

    if not meeting_json:
        return 404, "There is no any meeting"

    logging.debug("meetings json: " + str(meeting_json))
    meetings = Meetings.from_json(meeting_json)
    meeting = meetings.first

    time_to_start = round((meeting.date - datetime.now()).total_seconds() / 60.0)

    time_to_start, unit = __get_unit(time_to_start)
    return 200, (time_to_start, unit, meeting.name[:-4], meeting.link)


def __get_unit(time):
    if time == 1:
        return time, "minute"
    if time < 4 * 60:
        return time, "minutes"

    if time < 24 * 60:
        return round(time / 60), "hours"

    time = round(time / (24 * 60))
    if time < 48 * 60:
        return time, "day"
    return time, "days"


def get_config():
    return config


def validate(date):
    try:
        date = datetime.strptime(date, config["DATE_FORMAT"])
        return date
    except:
        return False
