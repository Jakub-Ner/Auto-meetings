import json
import logging
import shlex
import subprocess
import time
from datetime import datetime
from multiprocessing import Process
from threading import Thread

from .Meeting import Meeting
from .Meetings import Meetings
from variables.operating_systems.Ubuntu import open_page, open_obs, close_obs


class Opener:
    def __init__(self):
        self.sec_to_open = 0
        self.next_meeting = None
        self.waiting_thread = Process(target=self.__wait_for_meeting)

    def check_meeting(self, meeting: Meeting):
        if meeting == self.next_meeting or meeting is None:
            return False
        self.next_meeting = meeting
        self.sec_to_open = (meeting.date - datetime.now()).total_seconds()

        if self.waiting_thread.is_alive():
            self.waiting_thread.terminate()
            self.waiting_thread = Process(target=self.__wait_for_meeting)
        else:
            self.waiting_thread = Process(target=self.__wait_for_meeting)

        self.waiting_thread.start()

        if self.sec_to_open < 1:
            self.waiting_thread.terminate()
            try:
                subprocess.run(
                    shlex.split(f"notify-send 'Auto-meetings' '{meeting.name} starts in {self.sec_to_open} minutes'"))
                time.sleep(5)
            except Exception as exception:
                logging.error(f"Can't send notification: {exception}")

            run_meeting_thread = Thread(target=self.__run_meeting, args=(meeting,))
            run_meeting_thread.start()
            return True
        else:
            return False

    def __wait_for_meeting(self):
        time.sleep(self.sec_to_open)

    def __remove_meeting(self, meeting: Meeting):
        with open("variables/meetings.json", "r") as file:
            meetings = Meetings.from_json(json.load(file))

        meetings.remove(meeting.name)

        with open("variables/meetings.json", "w+") as data:
            json.dump(meetings.to_json(), data)

    def __run_meeting(self, meeting: Meeting):
        self.__remove_meeting(meeting)
        try:
            subprocess.run(shlex.split(f'{open_page} {meeting.link}'))
        except Exception as exception:
            logging.error(f"Can't open meeting: {exception}")

        try:
            subprocess.run(open_obs)
            time.sleep(60 * 60 * 2)
            try:
                subprocess.run(f'{close_obs}')

            except Exception as exception:
                logging.error(f"Can't close OBS: {exception}")

        except Exception as exception:
            logging.error(f"Can't open OBS: {exception}")


meeting_opener = Opener()
