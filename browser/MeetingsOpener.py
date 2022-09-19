import logging
import subprocess
import time
from datetime import datetime
from threading import Thread

import Meeting
from variables.operating_systems.Ubuntu import open_page, open_obs, close_obs


class Opener:
    def __init__(self):
        self.minutes_to_open = 0

    def check_meetings(self, meeting: Meeting):
        self.minutes_to_open = (meeting.date - datetime.now()).total_seconds() / 60.0
        if self.minutes_to_open < 1:
            try:
                subprocess.run(f"notify-send 'Auto-meetings' '{meeting.name} starts in {self.minutes_to_open} minutes'")
                time.sleep(5)
            except Exception as exception:
                logging.error(f"Can't send notification: {exception}")

            run_meeting_thread = Thread(target=self.run_meeting, args=(meeting,))
            run_meeting_thread.start()
            return True
        else:
            return False

    def run_meeting(self, meeting: Meeting):
        try:
            subprocess.run(f'{open_page}  {meeting.link}')
        except Exception as exception:
            logging.error(f"Can't open meeting: {exception}")

        try:
            subprocess.run(f'{open_obs}')
            time.sleep(60 * 60 * 2)
            try:
                subprocess.run(f'{close_obs}')

            except Exception as exception:
                logging.error(f"Can't close OBS: {exception}")

        except Exception as exception:
            logging.error(f"Can't open OBS: {exception}")


meeting_opener = Opener()
