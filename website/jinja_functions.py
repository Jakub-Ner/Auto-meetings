import json

def next():
        with open("variables/next_meeting.json", "r") as meeting:
            return meeting.read()

def delete(meeting_name):
    with open("variables/meetings.json", "r+") as meetings:
        meetings = json.load(meetings)
        meetings.pop(meeting_name)
