import json
import os
import time
import logging
import random

from variables.config import config
from .Mail import Mail
from .Meeting import Meeting
from .MeetingsOpener import meeting_opener
from .Meetings import Meetings


class Browser:
    def __init__(self):
        meetings_path = "variables/meetings.json"
        with open(meetings_path, "a+") as file:
            # if file is empty give necessary data
            if os.stat(meetings_path).st_size == 0:
                json.dump({}, file, indent=2)
                self.__meetings = Meetings()

        with open(meetings_path, "r") as data:
            self.__meetings = Meetings.from_json(json.load(data))

    counter = 0

    def search_meetings_periodically(self):
        if self.counter != 0:
            return
        self.counter += 1

        while True:
            self.search_meetings()
            time.sleep(3 * 60 * 60)

    def search_meetings(self):
        if config["searching_flag"]:
            logging.debug('Searching mode already on')
            return

        config["searching_flag"] = True
        logging.debug('started searching now')

        disposable_meetings = []

        mailbox = Mail()
        try:
            mailbox.log_in()
        except FileNotFoundError:
            logging.debug("Could not log in to mailbox")
            config["searching_flag"] = False
            return
        try:
            for email in self.get_emails():
                logging.debug(f"searching from {email}")
                urls, dates = mailbox.extract_data_from_mail(email)

                logging.debug(f"found {len(urls)} urls: {urls}")

                for i in range(len(urls)):
                    name = email + str(random.randint(1000, 10000))
                    disposable_meetings.append(Meeting(name, dates[i], urls[i]))

        except Exception as exception:
            logging.error(f'ERROR: Lack of internet connection! or {exception}')

        with open("variables/meetings.json", "r") as file:
            self.__meetings = Meetings.from_json(json.load(file))

        self.__meetings.add_many(disposable_meetings)

        logging.debug(f"added {len(disposable_meetings)} meetings")

        with open("variables/meetings.json", "w+") as data:
            json.dump(self.__meetings.to_json(), data)

        meeting_opener.check_meeting(self.__meetings.first)
        config["searching_flag"] = False
        logging.debug('Finished searching')

    def get_emails(self):
        emails = []
        meeting = self.__meetings.first
        while meeting is not None:
            if '@' in meeting.name and meeting.name not in emails:
                emails.append(meeting.name[:-4])
            meeting = meeting.next
        return emails
