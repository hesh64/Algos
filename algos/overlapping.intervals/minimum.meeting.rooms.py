"""
Minimum Meeting Rooms (hard) #
Given a list of intervals representing the start and end time of ‘N’ meetings,
 find the minimum number of rooms required to hold all the meetings.
"""

from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # the head uses the < property to sort
    def __lt__(self, other):
        return self.end < other.end


def get_min_room(meetings):
    # sort like we did before
    meetings.sort(key=lambda x: x.start)
    # this is clever.
    # ok so this is a min heap, remember when we defined __lt__
    # it's so that we can sort at log(n)
    min_heap = []
    # the largest the min head ever beed
    max_size = 0
    # iterate through the meetings
    for meeting in meetings:
        # push into the heap a meeting
        heappush(min_heap, meeting)
        # clear  our any meeting that ends BEFORE or AT THE SAME TIME the
        # meeting we just pushed ended
        while len(min_heap) and min_heap[0].end <= meeting.start:
            # pop pop - jimmy got shot
            heappop(min_heap)
        # anything left in the heap is a meeting that's taking place WHILE
        # the meeting we just pushed is at the very least starting
        max_size = max(len(min_heap), max_size)
    # return it. - give back.
    return max_size


def main():
    meetings = [Meeting(start, end) for start, end in [[1, 4], [2, 3], [3, 6]]]
    result = get_min_room(meetings=meetings)
    print(result)

    meetings = [Meeting(start, end) for start, end in [[4, 5], [2, 3], [2, 4], [3, 5]]]
    result = get_min_room(meetings=meetings)
    print(result)


main()
