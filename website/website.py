from flask import Blueprint, request
from flask.helpers import flash
import random

from werkzeug.exceptions import BadRequestKeyError

from .buttons import menu, delete
from .jinja_functions import base, validate, DATE_FORMAT, save_meetings

website = Blueprint("views", __name__)


@website.route("/", methods=['GET', 'POST'])
@base
def home(meetings):
    if request.method == 'POST':

        # buttons
        delete(meetings)
        menu(meetings)

        try:
            if not ((request.form["date"] and request.form["link"]) or request.form["name"]):
                flash("Meeting data is not sufficient", category="error")

            elif not (date := validate(request.form["date"])):
                flash("give date in format: DD-MM-YYYY hh:mm", category="error")

            else:
                name = request.form["name"] + str(random.randint(1000, 10000))

                try:
                    date = str(date.strftime(DATE_FORMAT))
                except: ...

                new_meeting = {name: {"date": date, "link": request.form["link"]}}
                meetings.update(new_meeting)
                save_meetings(meetings)

                flash("Meeting added", category="success")
        except BadRequestKeyError: ...
        except Exception as e:
            print(e)





