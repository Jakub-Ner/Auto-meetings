from flask import render_template
from datetime import datetime
import json

DATE_FORMAT = '%d-%m-%Y %H:%M'


def base(func):
    with open("variables/meetings.json", "r+") as meetings:
        meetings = json.load(meetings)

    def website(*args, **kwargs):
        func(meetings, *args, **kwargs)
        return render_template("base.html", meetings=meetings), 200

    website.__name__ = func.__name__
    return website


def save_meetings(meetings):
    with open("variables/meetings.json", "w+") as file:
        file.write(json.dumps(meetings))


def next():
    with open("variables/next_meeting.json", "r") as meeting:
        return json.load(meeting)


def get_config():
    with open("variables/config.json", "r") as config:
        return json.load(config)


def validate(date):
    try:
        date = datetime.strptime(date, DATE_FORMAT)
        return date
    except:
        return False
