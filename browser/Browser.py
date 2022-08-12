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
                json.dump({}, file, indent=2)
                self.__meetings = {}

            else:
                with open(VARIABLES_PATH + "meetings.json", "r") as data:
                    self.__meetings = json.load(data)

    def search_meetings_periodically(self):
        while True:
            self.search_meetings()
            time.sleep(3 * 60 * 60)

    def search_meetings(self):
        logging.info('echo start searching')
        disposable_meetings = {}

        mailbox = Mail()
        if not mailbox.log_in():
            return

        try:
            for email in self.get_emails():
                urls, dates = mailbox.read_mails(email)
                self.__meetings[email]["link"] = urls[0]
                self.__meetings[email]["date"] = dates[0]
                if dates:
                    dates[0][1] = convert_months_to_numbers(dates[0][1])  # e.g "lutego" into 2

                # add disposable meetings from all messages from email
                self.__meetings[email]["meetings"] = {}
                for i in range(1, len(urls)):
                    # key = str(email) + str(i)
                    key = create_key(email, i)
                    if dates:
                        dates[i][1] = convert_months_to_numbers(dates[i][1])
                    disposable_dict = {key: {"link": urls[i], "date": dates[i]}}
                    disposable_meetings.update(disposable_dict)

            # new mails will be added to the beginning of the list,
            # disposable links are added at the end, so If we meet one, we can finish the loop

            mailbox.log_out()
        except:
            logging.error('echo "ERROR: Lack of internet connection!"')

        self.__meetings.update(disposable_meetings)
        prepare_next_meeting(self.__meetings)

        with open(VARIABLES_PATH + "meetings.json", "w") as data:
            json.dump(self.__meetings, data, indent=2)

    def get_emails(self):
        emails = []
        for name in self.__meetings:
            if '@' in name and name not in emails:
                emails.append(name[:-4])
        return emails


def create_key(name, index):
    key = name.split('@')
    return key[0] + key[1] + str(index)
