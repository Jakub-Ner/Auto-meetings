import json
from datetime import datetime


class Meeting:
    def __init__(self, name, date, link, next=None):
        self.name = name
        if isinstance(date, str):
            self.date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        else:
            self.date = date
        self.link = link
        self.next = next

    def __gt__(self, other):
        return self.date > other.date


class MeetingEncoder(json.JSONEncoder):
    def default(self, o):
        json = {}
        for key in o.__dict__:
            if key != "date":
                json[key] = o.__dict__[key]
            else:
                json[key] = str(o.__dict__[key])
        return json


if __name__ == '__main__':
    meeting = Meeting('Plastyka', datetime(2020, 5, 1), 'www.plastyka.pl')

    meeting_json = json.dumps(meeting, cls=MeetingEncoder)

    print(meeting_json)

    meeting_dict = json.loads(meeting_json)

    meeting_obj = Meeting(**meeting_dict)
    print(meeting_obj)

    print(meeting_obj.date)
