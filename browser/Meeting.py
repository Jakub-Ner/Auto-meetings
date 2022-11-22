import json
from datetime import datetime
from variables.config import config


class Meeting:
    def __init__(self, name, date, link, next=None):
        self.name = name
        if isinstance(date, str):
            self.date = datetime.strptime(date, config['DATE_FORMAT'])
        else:
            self.date = date
        self.link = link
        self.next = next

    def __gt__(self, other):
        return self.date > other.date

    def __eq__(self, other):
        if isinstance(other, Meeting):
            return self.date == other.date and self.link == other.link
        return False


class MeetingEncoder(json.JSONEncoder):
    def default(self, o):
        _json = {}
        for key in o.__dict__:
            if key != "date":
                _json[key] = o.__dict__[key]
            else:
                _json[key] = o.__dict__[key].strftime(config['DATE_FORMAT'])
        return _json


if __name__ == '__main__':
    meeting = Meeting('Plastyka', datetime(2020, 5, 1), 'www.plastyka.pl')

    meeting_json = json.dumps(meeting, cls=MeetingEncoder)

    print(meeting_json)

    meeting_dict = json.loads(meeting_json)

    meeting_obj = Meeting(**meeting_dict)
    print(meeting_obj)

    print(meeting_obj.date)
