import logging
import json
from datetime import datetime

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

    def to_json(self):
        return json.dumps(self.__first, cls=MeetingEncoder, indent=3)

    @classmethod
    def from_json(cls, meetings_json):
        meeting_dict = json.loads(meetings_json)
        meeting = Meeting(**meeting_dict)
        return cls(meeting)

    def pop(self):
        if self.__first is None:
            logging.debug('Trying to pop from empty meetings list')
            return None

        meeting = self.__first
        self.__first = self.__first.next

        self.size -= 1
        return meeting

    def add(self, meeting: Meeting):
        self.size += 1
        if self.__first is None:
            self.__first = meeting
            return

        prev = self.__binsearch(meeting)
        tmp = prev.next
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

        return mid_meeting

    def __further(self, meeting: Meeting, mid_idx):
        for i in range(mid_idx):
            meeting = meeting.next
        return meeting


if __name__ == '__main__':
    m1 = Meeting('Plastyka', datetime(2020, 5, 1), 'www.plastyka.pl')
    m2 = Meeting('biologia', datetime(2020, 5, 20), 'www.plastyka.pl')
    m3 = Meeting('matma', datetime(2020, 5, 13), 'www.plastyka.pl')
    m4 = Meeting('matma', datetime(2020, 5, 11), 'www.plastyka.pl')
    m5 = Meeting('matma', datetime(2020, 5, 18), 'www.plastyka.pl')
    m6 = Meeting('matma', datetime(2020, 5, 21), 'www.plastyka.pl')
    m7 = Meeting('matma', datetime(2020, 5, 20), 'www.plastyka.pl')
    m8 = Meeting('matma', datetime(2020, 5, 1), 'www.plastyka.pl')
    m9 = Meeting('matma', datetime(2020, 5, 13), 'www.plastyka.pl')
    m10 = Meeting('matma', datetime(2020, 5, 7), 'www.plastyka.pl')

    meetings = Meetings(m1)
    meetings.add(m2)
    meetings.add(m3)
    meetings.add(m4)
    meetings.add(m5)
    meetings.add(m6)
    meetings.add(m7)
    meetings.add(m8)
    meetings.add(m9)
    meetings.add(m10)

    meetings_json = meetings.to_json()
    obj = Meetings.from_json(meetings_json)

    print(meetings.last.date)
