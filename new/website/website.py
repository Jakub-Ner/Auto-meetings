from flask import Blueprint, render_template, request, jsonify
from flask.helpers import flash
import json

website = Blueprint("views", __name__)

@website.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if not note:
            flash("note is too short", category="error")
        else:
            flash("note added", category="success")

    return render_template("base.html", user="current_user")


@website.route("/delete-note", methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note["noteId"]
    return jsonify({})
