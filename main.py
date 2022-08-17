import threading
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from browser.Browser import Browser
browser = Browser()

from website import create_app

app = create_app()

if __name__ == "__main__":
    meeting_from_mails = threading.Thread(target=browser.search_meetings_periodically)
    meeting_from_mails.start()

    app.run(debug=True)
    meeting_from_mails.join()
