import logging
import json

from .Meeting import Meeting, MeetingEncoder


class Meetings:
    def __init__(self, first: Meeting = None):
        self.__first = first
        if first is not None:
            self.size = 1
        else:
            self.size = 0

    @property
    def first(self):
        return self.__first

    def to_list(self):
        if self.__first is None:
            return []

        meetings_list = []
        next_meeting = self.to_json().copy()
        while next_meeting is not None:
            meeting = next_meeting
            next_meeting = meeting.pop('next')
            meetings_list.append(meeting)
        return meetings_list

    def to_json(self):
        return json.loads(json.dumps(self.__first, cls=MeetingEncoder, indent=3))

    @classmethod
    def from_json(cls, meetings_json):
        if not meetings_json:
            return cls()

        prev_json = meetings_json
        meetings_obj = cls(Meeting(**prev_json))
        prev_obj = meetings_obj.first

        while prev_json["next"] is not None:
            prev_json = prev_json["next"]
            prev_obj.next = (Meeting(**prev_json))
            prev_obj = prev_obj.next

        return meetings_obj

    def remove(self, name):
        print(self.__first.name)
        if self.__first is None:
            logging.debug('Trying to remove from empty meetings list')
            return

        if self.__first.name == name:
            self.__first = self.__first.next
            self.size -= 1
            return

        prev = self.__first
        while prev.next is not None:
            if prev.next.name == name:
                prev.next = prev.next.next
                self.size -= 1
                return
            prev = prev.next

        logging.error(f'No meeting with name {name} found')

    def pop(self):
        if self.__first is None:
            logging.debug('Trying to pop from empty meetings list')
            return None

        meeting = self.__first
        self.__first = self.__first.next

        self.size -= 1
        return meeting

    def add_many(self, new_meetings: list):
        for meeting in new_meetings:
            self.add(meeting)

    def add(self, meeting: Meeting):
        self.size += 1
        if self.__first is None:
            self.__first = meeting
            return

        prev, idx = self.__binsearch(meeting)
        if idx <= 0:
            tmp = self.__first
            if tmp == meeting:
                self.size -= 1
                return
            self.__first = meeting
        else:
            tmp = prev.next
            if tmp == meeting:
                self.size -= 1
                return
            prev.next = meeting
        meeting.next = tmp

    def __binsearch(self, meeting: Meeting):
        first_idx = 0
        last_idx = self.size - 2  # -2 because of line 38

        mid_idx = (last_idx + first_idx) // 2
        mid_meeting = self.__further(self.__first, mid_idx)

        while first_idx <= last_idx:
            if meeting > mid_meeting:
                first_idx = mid_idx + 1
                mid_idx = (last_idx + first_idx) // 2
                mid_meeting = self.__further(mid_meeting, mid_idx - first_idx + 1)
            else:
                last_idx = mid_idx - 1
                mid_idx = (last_idx + first_idx) // 2
                mid_meeting = self.__further(self.__first, mid_idx)

        return mid_meeting, mid_idx

    def __further(self, meeting: Meeting, mid_idx):
        for i in range(mid_idx):
            meeting = meeting.next
        return meeting


if __name__ == '__main__':
    # d = {'name': 'kubaner1@gmail.com7404', 'date': '28-03-2025 10:11', 'link': 'https://stackoverflow.com/',
    #      'next': {'name': 'kubaner1@gmail.com1998', 'date': '22-11-2022 13:00',
    #               'link': 'link:\r\nhttps://meet.google.com/hcd-mrsc-irp\r\notherwise,',
    #               'next': {'name': 'kubaner1@gmail.com2256', 'date': '22-11-2022 13:00',
    #                        'link': 'link:\r\nhttps://meet.google.com/hcd-mrsc-irp\r\notherwise,', 'next': None}}}
    #
    d = {"name": "kubaner1@gmail.com9224",
         "date": "28-03-2023 10:11",
         "link": "https://stackoverflow.com/",
         "next": None}
    m = Meetings().from_json(d)
    m.add(Meeting("kubaner1@gmail.com4902", "22-11-2022 13:00", "dupa.pl"))
    print(m.to_json())
    m.add(Meeting("kubaner1@gmail.com4902", "22-11-2022 13:00", "dupa.pl"))
    print(m.to_json())
    # m.remove('kubaner1@gmail.com1998')
    # m1 = Meeting('Plastyka', datetime(2020, 5, 1), 'www.plastyka.pl')
    # m2 = Meeting('biologia', datetime(2020, 5, 20), 'www.plastyka.pl')
    # m3 = Meeting('matma', datetime(2020, 5, 13), 'www.plastyka.pl')
    # m4 = Meeting('matma', datetime(2020, 5, 11), 'www.plastyka.pl')
    # m5 = Meeting('matma', datetime(2020, 5, 18), 'www.plastyka.pl')
    # m6 = Meeting('matma', datetime(2020, 5, 21), 'www.plastyka.pl')
    # m7 = Meeting('matma', datetime(2020, 5, 20), 'www.plastyka.pl')
    # m8 = Meeting('matma', datetime(2020, 5, 1), 'www.plastyka.pl')
    # m9 = Meeting('matma', datetime(2020, 5, 13), 'www.plastyka.pl')
    # m10 = Meeting('matma', datetime(2020, 5, 7), 'www.plastyka.pl')
    #
    # meetings = Meetings(m1)
    # meetings.add(m2)
    # meetings.add(m3)
    # meetings.add(m4)
    # meetings.add(m5)
    # meetings.add(m6)
    # meetings.add(m7)
    # meetings.add(m8)
    # meetings.add(m9)
    # meetings.add(m10)

    # meetings_json = meetings.to_json()
    # print(meetings_json, type(meetings_json))
    # meetings_list = meetings.to_list()
    # print(len(meetings_list), type(meetings_list))
    # obj = Meetings.from_json(meetings_json)
    # print(obj.to_json())
    # print(meetings.first.date)
