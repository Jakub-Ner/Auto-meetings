from datetime import datetime

date = '28-03-2002 10:11'
date = datetime.strptime(date, '%d-%m-%Y %H:%M')
import json


def next():
    with open("variables/next_meeting.json", "r") as meeting:
        return meeting.read()


def get_config():
    with open("variables/config.json", "r") as config:
        return json.load(config)

print(next())
print(get_config())
if __name__ == '__main__':
    ...
