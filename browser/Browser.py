import json
import os
import time
import logging
from .Mail import Mail
from .manage_dates import convert_months_to_numbers, prepare_next_meeting

VARIABLES_PATH = os.path.dirname(os.path.abspath(__file__)) + f"/../variables/"


class Browser:
    def __init__(self):
        with open(VARIABLES_PATH + "meetings.json", "w+") as file:
            # if file is empty give necessary data
            if os.stat(VARIABLES_PATH + "meetings.json").st_size == 0:
                necessary_data = {
                    "@1234": {
                        "date": "40-13-1900 25:61",  # DD-MM-YYYY hh:mm
                        "link": ""
                    }}
                json.dump(necessary_data, file, indent=2)
                self.meetings = necessary_data

            else:
                with open(VARIABLES_PATH + "meetings.json", "r") as data:
                    self.meetings = json.load(data)

    @staticmethod
    def __create_key(name, index):
        key = name.split('@')
        return key[0] + key[1] + str(index)

    def search_meetings_periodically(self):
        while True:
            self.search_meetings()
            time.sleep(3 * 60 * 60)

    def search_meetings(self):
        logging.info('echo start searching')
        disposable_meetings = {}

        mail = Mail()
        if not mail.log_in():
            return

        try:
            mail.mail.select('inbox')

            for mail in self.meetings:
                if len(mail) > 1:
                    if "@" in mail:
                        urls, dates = mail.read_mails(mail)
                        self.meetings[mail]["link"] = urls[0]
                        self.meetings[mail]["date"] = dates[0]
                        if dates:
                            dates[0][1] = convert_months_to_numbers(dates[0][1])  # e.g "lutego" into 2

                        # add disposable meetings from all messages from mail
                        self.meetings[mail]["meetings"] = {}
                        for i in range(1, len(urls)):
                            # key = str(mail) + str(i)
                            key = self.__create_key(mail, i)
                            if dates:
                                dates[i][1] = convert_months_to_numbers(dates[i][1])
                            disposable_dict = {key: {"link": urls[i], "date": dates[i]}}
                            disposable_meetings.update(disposable_dict)

                    # new mails will be added to the beginning of the list,
                    # disposable links are added at the end, so If we meet one, we can finish the loop
                    else:
                        break

            mail.end()
        except:
            logging.error('echo "ERROR: Lack of internet connection!"')

        self.meetings.update(disposable_meetings)
        prepare_next_meeting(self.meetings)

        with open(VARIABLES_PATH + "meetings.json", "w") as data:
            json.dump(self.meetings, data, indent=2)
