class Miner:
    def __init__(self, text):
        self.language = self.find_language(text)
        self.date = self.find_date(text)
        self.link = self.find_link(text)

    def find_language(self, text):
        ...

    def find_date(self, text):
        ...

    def find_link(self, text):
        ...
