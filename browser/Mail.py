import logging

# from .TOP_SECRET import PASS, MY_MAIL
MY_MAIL = 'kulfoner@gmail.com'
PASS = 'kulPHONE_1'

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
            print(MY_MAIL, PASS)
            try:
                self.__mail.login(MY_MAIL, PASS)
                self.__mail.select('inbox')
                return True

            except imaplib.IMAP4.error:
                logging.error(f'echo "ERROR: Invalid login or password! from {self.__sender}"')

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


if __name__ == '__main__':
    mailbox = Mail()
    if not mailbox.log_in():
        exit(1)

    data = mailbox.read_mails("kubaner1@gmail.com")
    print(data)

import os.path
import base64
import json
import re
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import logging
import requests

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def readEmails():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file('my_cred_file.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
        messages = results.get('messages', [])
        if not messages:
            print('No new messages.')
        else:
            message_count = 0
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                email_data = msg['payload']['headers']
                for values in email_data:
                    name = values['name']
                    if name == 'From':
                        from_name = values['value']
                        for part in msg['payload']['parts']:
                            try:
                                data = part['body']["data"]
                                byte_code = base64.urlsafe_b64decode(data)

                                text = byte_code.decode("utf-8")
                                print("This is the message: " + str(text))

                                # mark the message as read (optional)
                                msg = service.users().messages().modify(userId='me', id=message['id'],
                                                                        body={'removeLabelIds': ['UNREAD']}).execute()
                            except BaseException as error:
                                pass
    except Exception as error:
        print(f'An error occurred: {error}')
