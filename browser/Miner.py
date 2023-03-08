from datetime import datetime
import logging
import datefinder


class Miner:
    def __init__(self, text):
        text = text.lower()
        self.language = self.find_language(text)
        self.date = self.find_date(text)
        self.link = self.find_link(text)
        logging.debug(f'found: Language: {self.language}, Date: {self.date}, Link: {self.link}')

    def find_language(self, text):
        # Here, You can add more dictionaries/special characters for other languages
        pl = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', ]

        if language := self.__find_language_helper(text, pl, 'pl'):
            return language
        return 'en'

    def __find_language_helper(self, text, dictionary, language):
        for letter in dictionary:
            if letter in text:
                return language

    def find_link(self, text):
        domains = ['meet.google', 'zoom.', 'teams.microsoft']

        words = text.replace('\n', ' ').replace('\r', ' ').split(' ')
        # find first word that contains domain
        for word in words:
            for domain in domains:
                if domain in word:
                    return word

        return None

    def find_date(self, text):
        date = list(datefinder.find_dates(text))
        logging.info(f'Dates found: {date}')
        date = date[2 % len(date)]

        if self.language == 'en':
            if date.date() < datetime.now().date():
                return None
            return date

        # date may have incorrect month
        if self.language == 'pl':
            months = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'września',
                      'października', 'listopada', 'grudnia']
            for i, month in enumerate(months):
                if month in text:
                    return date.replace(month=(i + 1))

        if date.date() < datetime.now().date():
            return None
        return date


if __name__ == '__main__':
    miner = Miner(
        'For English scroll down 20 09 2022 13:15 https://pwr-edu.zoom.us/j/93305685440?pwd=MmhNYmdhMWrweZsWjI3R1dZbjh6QT0 '
    )
    print(miner.language)
    print(miner.link)
    print(miner.date)
