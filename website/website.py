from flask import Blueprint, render_template, request, jsonify
from flask.helpers import flash
import json

website = Blueprint("views", __name__)

@website.route("/", methods=['GET', 'POST'])
def home():
    with open("variables/meetings.json", "r+") as meetings:
        meetings = json.load(meetings)
        
        if request.method == 'POST':
            new_meeting = eval(request.form.get('meeting'))
                    
            if not new_meeting:
                flash("note is too short", category="error")
            else:
                meetings.update(new_meeting)

                with open("variables/meetings.json", "w+") as file:
                    file.write(json.dumps(meetings))

                flash("note added", category="success")


        print(meetings)
        return render_template("base.html", meetings=meetings)


@website.route("/delete-note", methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note["noteId"]
    return jsonify({})
