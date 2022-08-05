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


def next_meeting():
    with open("variables/next_meeting.json", "r") as meeting:
        meeting = json.load(meeting)
        name = list(meeting.keys())[0]
        meeting_start = date = datetime.strptime(meeting[name]["date"], '%d-%m-%Y %H:%M')

    current_time = datetime.now()
    time_to_start = round((meeting_start - current_time).total_seconds() / 60.0)
    time_to_start, unit = __get_unit(time_to_start)
    return time_to_start, unit, name[:-4], meeting[name]["link"]


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
    with open("variables/config.json", "r") as config:
        return json.load(config)


def validate(date):
    try:
        date = datetime.strptime(date, DATE_FORMAT)
        return date
    except:
        return False
