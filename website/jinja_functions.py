
def next():
        with open("variables/next_meeting.json", "r") as meeting:
            return meeting.read()