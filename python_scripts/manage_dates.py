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
    while (i < len(KEYS)):
        if (KEYS[i] in month):
            return MONTHS[KEYS[i]]
        i += 1


def prepare_next_meeting(meetings):
    next_meeting_name = __find_next_meeting__(meetings)
    __save_next_meeting__(meetings[next_meeting_name], next_meeting_name)
    # if meeting is disposable delete it
    if not '@' in next_meeting_name:
        meetings.pop(next_meeting_name)


def __save_next_meeting__(meeting, name):
    with open('variables/next_meeting.txt', 'w') as fin:

        fin.write(name)
        fin.write("\n")

        for date_part in meeting["date"]:
            fin.write(str(date_part))
            fin.write(" ")
        fin.write("\n")

        fin.write(meeting["link"])


def __find_next_meeting__(meetings):
    next_meeting_name = list(meetings.keys())[0]

    for meeting in meetings:
        # comparing year of meeting
        if meetings[meeting]["date"][2] < meetings[next_meeting_name]["date"][2]:
            next_meeting_name = meeting
            continue

        # comparing month of meeting
        if meetings[meeting]["date"][1] < meetings[next_meeting_name]["date"][1]:
            next_meeting_name = meeting
            continue

        # comparing day of meeting
        if meetings[meeting]["date"][0] < meetings[next_meeting_name]["date"][0]:
            next_meeting_name = meeting
            continue

        # meeting["date"][3] = "hh:mm", so:
        # comparing hour of meeting
        if meetings[meeting]["date"][3][0:2] < meetings[next_meeting_name]["date"][3][0:2]:
            next_meeting_name = meeting
            continue

        # comparing minute of meeting
        if meetings[meeting]["date"][3][3:5] < meetings[next_meeting_name]["date"][3][3:5]:
            next_meeting_name = meeting

    return next_meeting_name
