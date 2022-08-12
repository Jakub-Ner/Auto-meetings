import logging

from .TOP_SECRET import PASS, MY_MAIL
import imaplib
import email


class Mail:
    def __init__(self):
        self.__SMTP_PORT = 993
        self.__SMTP_SERVER = "imap.gmail.com"
        self.__mail = imaplib.IMAP4_SSL(self.__SMTP_SERVER)
        self.__sender = ""

    def log_in(self):
        if MY_MAIL and PASS:
            self.__mail.login(MY_MAIL, PASS)
            self.__mail.select('inbox')
            return True
        return False

    def read_mails(self, email_from):
        self.__sender = email_from
        data = self.__mail.search(None, 'FROM', self.__sender)
        ids = data[1][0].split()
        ids.reverse()

        links = []
        dates = []
        for i in ids:
            data = self.__mail.fetch(str(int(i)), '(RFC822)')
            state, response_part = data
            message = str(email.message_from_string(str(response_part[0][1], "utf-8")).get_payload(0))
            link, date = self.__find_data(message)

            if link and date:
                links.append(link)
                dates.append(date)
        return links, dates

    def log_out(self):
        self.__mail.close()
        self.__mail.logout()

    def __find_data(self, message):
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
                    logging.error(f'echo "ERROR: Invalid date format in mail! from {self.__sender}"')

        return "", []
