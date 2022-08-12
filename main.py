import threading
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from website import create_app
from browser.Browser import Browser

app = create_app()

if __name__ == "__main__":
    browser = Browser()
    meeting_from_mails = threading.Thread(target=browser.search_meetings_periodically)
    meeting_from_mails.start()

    app.run(debug=True)
    meeting_from_mails.join()
