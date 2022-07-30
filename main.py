import threading

from website import create_app
from python_scripts.get_links_from_mails import search_meetings_periodically

app = create_app()



if __name__ == "__main__":
    meeting_from_mails = threading.Thread(target=search_meetings_periodically)
    meeting_from_mails.start()

    app.run(debug=True)
    meeting_from_mails.join()
