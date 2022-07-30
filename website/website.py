from flask import Blueprint, render_template, request, jsonify
from flask.helpers import flash
import json
import subprocess
import shlex
import random
website = Blueprint("views", __name__)


@website.route("/", methods=['GET', 'POST'])
def home():
    with open("variables/meetings.json", "r+") as meetings:
        meetings = json.load(meetings)
        print("cokolwiek")
        if request.method == 'POST':
            try:
                if request.form["sign-in"]:
                    subprocess.run(shlex.split("sudo gedit ./python_scripts/TOP_SECRET.py"))
            except Exception as e:
                pass
                # print(e)  # <- not sure
            try:
                if request.form["delete"]:
                    print("ok")
                    print(request.form["delete"])
            except Exception as e: print("nie pytklo")

            try:
                if not request.form["date"] or not request.form["link"]:
                    flash("Meeting data is not sufficient", category="error")

                else:
                    name = request.form["name"] + str(random.randint(1000, 10000))
                    new_meeting = {name: {"date": request.form["date"], "link": request.form["link"]}}
                    meetings.update(new_meeting)

                    with open("variables/meetings.json", "w+") as file:
                        file.write(json.dumps(meetings))

                    flash("Meeting added", category="success")

            except Exception as e:
                print(e)

        return render_template("base.html", meetings=meetings)


@website.route("/delete-note", methods=['POST'])
def delete_note():
    print("delete")
    note = json.loads(request.data)
    noteId = note["noteId"]
    return jsonify({})
