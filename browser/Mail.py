import base64
import logging

from .Auth import Auth
from .Miner import Miner


class Mail(Auth):

    def extract_data_from_mail(self, sender):
        links = []
        dates = []

        try:
            results = self.service.users().messages() \
                .list(userId='me', labelIds=['INBOX'], q=f"from:{sender}").execute()
            messages = results.get('messages', [])

            for message in messages[:min(5, len(messages) - 1)]:
                text = self.__read_message(message)
                if text is None:
                    continue

                miner = Miner(text)
                if miner.link and miner.date:
                    links.append(miner.link)
                    dates.append(miner.date)
            return links, dates

        except Exception as error:
            logging.error(f'An error occurred: {error}')

    def __read_message(self, message):
        msg = self.service.users().messages().get(userId='me', id=message['id']).execute()
        email_data = msg['payload']['headers']
        for values in email_data:
            name = values['name']
            if name == 'From':
                from_name = values['value']
                logging.debug(f'Reading email from {from_name}')

                for part in msg['payload']['parts']:
                    try:
                        data = part['body']["data"]
                        byte_code = base64.urlsafe_b64decode(data)
                        text = byte_code.decode("utf-8")
                        return text

                    except BaseException as _:
                        pass
