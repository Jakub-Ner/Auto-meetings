import imaplib
from TOP_SECRET import PASS, MY_MAIL, LECTURES
import email
import json


class Mail:
    def __init__(self):
        self.MY_EMAIL = MY_MAIL
        self.MY_PASS = PASS
        self.SMTP_PORT = 993
        self.SMTP_SERVER = "imap.gmail.com"

        self.mail = imaplib.IMAP4_SSL(self.SMTP_SERVER)
        self.mail.login(self.MY_EMAIL, self.MY_PASS)

    def read_mails(self, FROM):
        self.mail.select('inbox')
        data = self.mail.search(None, 'FROM', FROM)
        ids = data[1][0].split()
        ids.reverse()
        message = "";
        link = ""
        for i in ids:
            data = self.mail.fetch(str(int(i)), '(RFC822)')
            state, response_part = data
            message = str(email.message_from_string(str(response_part[0][1], "utf-8")).get_payload(0))
            link, date = self.find_data(message)
            if link:
                break
        return link, date

    def find_data(self, message):
        words = message.split()
        for i, word in enumerate(words):
            if "terminie" in word:
                date = [words[i + j] for j in range(1, 5)]
                for i in range(i + 4, len(words)):
                    if "https://pwr-edu.zoom" in words[i]:  # <- to repair
                        return words[i], date
        return "", []

    def end(self):
        self.mail.close()
        self.mail.logout()


lectures = LECTURES

M = Mail()
for mail in lectures:
    if ("@" in mail):
        url, date = M.read_mails(mail)
        lectures[mail]["link"] = url
        lectures[mail]["date"] = date

M.end()

with open("lectures.json", "w") as data:
    json.dump(lectures, data, indent=2)
