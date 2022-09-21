import threading
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from browser import browser
from website import create_app

import logging
logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = create_app()

if __name__ == "__main__":
    meeting_from_mails = threading.Thread(target=browser.search_meetings_periodically)
    meeting_from_mails.start()

    app.run(debug=True)
    meeting_from_mails.join()
