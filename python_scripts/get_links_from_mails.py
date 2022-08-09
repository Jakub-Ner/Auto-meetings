import json
import os
import time

from .Mail import Mail
from .manage_dates import convert_months_to_numbers, prepare_next_meeting

MEETINGS_PATH = os.path.dirname(os.path.abspath(__file__)) + f"/../variables/meetings.json"


def __create_key(name, index):
    key = name.split('@')
    return key[0] + key[1] + str(index)


def search_meetings_periodically():
    while True:
        search_meetings()
        time.sleep(3 * 60 * 60)


def search_meetings():
    os.system('echo start searching')
    # if file didn't exist a+ creates it
    with open(MEETINGS_PATH, "a+") as file:
        # if file is empty give necessary data
        if os.stat(MEETINGS_PATH).st_size == 0:
            necessary_data = {
                "@1234": {
                    "date": [
                        40,  # day
                        13,  # month
                        2222,  # year
                        "25:62"  # hour:minute
                    ],
                    "link": ""
                }}
            json.dump(necessary_data, file, indent=2)

    # if you want to run only python scripts change MEETINGS_PATH to
    # "../variables/meetings.json"
    with open(MEETINGS_PATH, "r") as data:
        meetings = json.load(data)

    try:
        M = Mail()
        M.mail.select('inbox')

        disposable_meetings = {}
        for mail in meetings:
            if len(mail) > 1:
                if "@" in mail:
                    urls, dates = M.read_mails(mail)
                    meetings[mail]["link"] = urls[0]
                    meetings[mail]["date"] = dates[0]
                    if dates:
                        dates[0][1] = convert_months_to_numbers(dates[0][1])  # e.g "lutego" into 2

                    # add disposable meetings from all messages from mail
                    meetings[mail]["meetings"] = {}
                    for i in range(1, len(urls)):
                        # key = str(mail) + str(i)
                        key = __create_key(mail, i)
                        if dates:
                            dates[i][1] = convert_months_to_numbers(dates[i][1])
                        disposable_dict = {key: {"link": urls[i], "date": dates[i]}}
                        disposable_meetings.update(disposable_dict)

                # new mails will be added to the beginning of the list,
                # disposable links are added at the end, so If we meet one, we can finish the loop
                else:
                    break

        M.end()
    except:
        os.system('echo "ERROR: Lack of internet connection!"')

    meetings.update(disposable_meetings)
    os.system(f'echo {len(meetings)}')

    prepare_next_meeting(meetings)

    with open(MEETINGS_PATH, "w") as data:
        json.dump(meetings, data, indent=2)
