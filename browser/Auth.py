import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.exceptions import RefreshError
import logging


class Auth:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
        self.token_path = 'browser/credentials/token.json'
        self.creds = None
        self.service = None

    def log_in(self):
        if os.path.exists(self.token_path):
            self.creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                try:
                    self.creds.refresh(Request())
                except RefreshError as error:
                    logging.error(str(error))
                    self.__authorize()
            else:
                self.__authorize()

            # with open(self.token_path, 'w+') as token:
            #     token.write(self.creds.to_json())

        self.service = build('gmail', 'v1', credentials=self.creds)

    def __authorize(self):
        credentials_path = 'browser/credentials/credentials.json'

        if os.path.exists(credentials_path):
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, self.SCOPES)
            self.creds = flow.run_local_server(port=0)
        else:
            logging.error(
                f'ERROR: {credentials_path} is missing! Please contact kubaner1@gmail.com in order to get it.')

