import os

MONTHS = {"stycz": 1,
          "lut": 2,
          "mar": 3,
          "kwie": 4,
          "maj": 5,
          "czerw": 6,
          "lip": 7,
          "sierp": 8,
          "wrze": 9,
          "dziernik": 10,
          "listopad": 11,
          "grud": 12}

KEYS = list(MONTHS.keys())


def convert_months_to_numbers(month):
    i = 0
    while i < len(KEYS):
        if KEYS[i] in month:
            return MONTHS[KEYS[i]]
        i += 1


def prepare_next_meeting(meetings):
    next_meeting_name = __find_next_meeting__(meetings)
    __save_next_meeting__(meetings[next_meeting_name], next_meeting_name)
    # if meeting is disposable delete it


def __save_next_meeting__(meeting, name):
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    with open(absolute_path + '/../variables/next_meeting.json', 'w+') as fin:
        fin.write(name)
        fin.write("\n")

        for date_part in meeting["date"]:
            fin.write(" ")
            fin.write(str(date_part))
        fin.write("\n")

        fin.write(meeting["link"])


def __find_next_meeting__(meetings):
    next_meeting_name = "@"  # <- empty meeting
    trash = []

    for meeting in meetings:

        if (meetings[meeting]["date"] == []) or \
                ((meeting != '@') and (not __check_if_meeting_isnt_old(meetings[meeting]["date"]))):
            trash.append(meeting)

        else:
            # comparing year of meeting
            c = compare(meetings[meeting]["date"][2], meetings[next_meeting_name]["date"][2])
            if c == 1:
                next_meeting_name = meeting
                continue
            if c == -1:
                continue

            # comparing month of meeting
            c = compare(meetings[meeting]["date"][1], meetings[next_meeting_name]["date"][1])
            if c == 1:
                next_meeting_name = meeting
                continue
            if c == -1:
                continue

            # comparing day of meeting
            c = compare(meetings[meeting]["date"][0], meetings[next_meeting_name]["date"][0])
            if c == 1:
                next_meeting_name = meeting
                continue
            if c == -1:
                continue

            # comparing hour of meeting
            # meeting["date"][3] = "hh:mm", so:
            c = compare(int(meetings[meeting]["date"][3][0:2]), int(meetings[next_meeting_name]["date"][3][0:2]))
            if c == 1 :
                next_meeting_name = meeting
                continue
            if c == -1:
                continue

            # comparing minute of meeting
            if meetings[meeting]["date"][3][3:5] < meetings[next_meeting_name]["date"][3][3:5]:
                next_meeting_name = meeting

    # delete all old meetings from the list
    for t in trash:
        if '@' in t and len(t) > 1:
            meetings[t]["date"] = []
        else:
            meetings.pop(t)

    return next_meeting_name