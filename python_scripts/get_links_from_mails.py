import imaplib
import email
import json
import os

from TOP_SECRET import PASS, MY_MAIL
from manage_dates import convert_months_to_numbers, prepare_next_meeting

MEETINGS_PATH = f"../variables/meetings.json"


class Mail:
    def __init__(self):
        self.MY_EMAIL = MY_MAIL
        self.MY_PASS = PASS
        self.SMTP_PORT = 993
        self.SMTP_SERVER = "imap.gmail.com"

        self.mail = imaplib.IMAP4_SSL(self.SMTP_SERVER)
        self.mail.login(self.MY_EMAIL, self.MY_PASS)

        self.email_from = ""

    def read_mails(self, email_from):
        self.email_from = email_from
        data = self.mail.search(None, 'FROM', self.email_from)
        ids = data[1][0].split()
        ids.reverse()

        links = []
        dates = []
        for i in ids:
            data = self.mail.fetch(str(int(i)), '(RFC822)')
            state, response_part = data
            message = str(email.message_from_string(str(response_part[0][1], "utf-8")).get_payload(0))
            link, date = self.find_data(message)
            if link:
                links.append(link)
                dates.append(date)
        return links, dates

    def find_data(self, message):
        words = message.split()
        for i, word in enumerate(words):
            if "termin" in word:
                try:
                    date = []
                    for j in range(1, 5):
                        if j % 2 == 1:
                            date.append(int(words[i + j]))  # day and year
                        else:
                            date.append(words[i + j])  # month and hh:mm

                    # this below doesn't make sense
                    for i in range(i + 4, len(words)):
                        if "https://pwr-edu.zoom" in words[i]:  # <- to repair
                            return words[i], date

                except:
                    os.system('echo "ERROR: Invalid date format in mail! from {}"'.format(self.email_from))

        return "", []

    def end(self):
        self.mail.close()
        self.mail.logout()


def create_key(name, index):
    key = name.split('@')
    return key[0] + key[1] + str(index)

if __name__ == "__main__":

    # if file didn't exist a+ creates it
    with open(MEETINGS_PATH, "a+") as file:
        # if file is empty give necessary data
        if os.stat(MEETINGS_PATH).st_size == 0:
            necessary_data = {
                "@": {
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
                        key = create_key(mail, i)
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
    prepare_next_meeting(meetings)

    # if you want to run only python scripts change path to
    # "../variables/meetings.json"
    with open(MEETINGS_PATH, "w") as data:
        json.dump(meetings, data, indent=2)
