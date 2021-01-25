"""Problem Statement #
Given a list of intervals, merge all the overlapping
intervals to produce a list that has only mutually exclusive intervals.

"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print(self):
        print(f'[{self.start},{self.end}]')

    def __repr__(self):
        return f'[{self.start}, {self.end}]'


def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)
    start, end = intervals[0].start, intervals[0].end

    merged = []

    for i in range(1, len(intervals)):
        interval = intervals[i]

        if end >= interval.start:
            end = max(end, interval.end)
        else:
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged.append(Interval(start, end))
    return merged


def any_overlap(intervals):
    if len(intervals) < 2:
        return False

    intervals.sort(key=lambda x: x.start)

    start, end = intervals[0].start, intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if end >= interval.start:
            return True
        else:
            start, end = interval.start, interval.end

    return False


# apparently because the list is sorted we should come up with a solution
# that's better than O(n*log(n))
# ok noew it's O(n)
def insert_interval(intervals, new):
    merged_ = []

    i = 0
    while i < len(intervals) and intervals[i].end < new.start:
        merged_.append(intervals[i])
        i += 1

    start, end = new.start, new.end

    while i < len(intervals) and end >= intervals[i].start:
        end = max(end, intervals[i].end)
        start = min(start, intervals[i].start)
        i += 1

    merged_.append(Interval(start, end))

    while i < len(intervals):
        merged_.append(intervals[i])
        i += 1

    return merged_


"""
Problem Statement #
Given two lists of intervals, find the intersection of these two lists. 
Each list consists of disjoint intervals sorted on their start time.
"""


def merge(inter_a, inter_b):
    i, j = 0, 0
    intersections = []

    while i < len(inter_a) and j < len(inter_b):
        a_overlaps_b = inter_b[j].start <= inter_a[i].start <= inter_b[j].end
        b_overlaps_a = inter_a[i].start <= inter_b[j].start <= inter_a[i].end

        if a_overlaps_b or b_overlaps_a:
            intersections.append(Interval(max(inter_a[i].start, inter_b[j].start), min(inter_a[i].end, inter_b[j].end)))

        if inter_a[i].end < inter_b[j].end:
            i += 1
        else:
            j += 1

    return intersections


"""
Given an array of intervals representing ‘N’ appointments, find
out if a person can attend all the appointments.
"""


def find_conflicting_appointments(intervals):
    intervals.sort(key=lambda x: x.start)

    for i in range(0, len(intervals) - 1):
        if intervals[i].end > intervals[i + 1].start:
            return False

    return True


"""
Minimum Meeting Rooms (hard) #
Given a list of intervals representing the start and end time of ‘N’ meetings, 
find the minimum number of rooms required to hold all the meetings.
"""


def minimum_meeting_rooms(intervals):
    # first we gotta sort
    intervals.sort(key=lambda x: x.start)

    i = 0
    merged = [intervals[i]]
    i += 1
    while i < len(intervals):
        if merged[-1].end > intervals[i].start:
            merged[-1].end = max(merged[-1].end, intervals[i].end)
        else:
            merged.append(intervals[i])
        i += 1

    return len(merged) - len(intervals)


def main():
    res = merge_intervals([Interval(1, 4), Interval(2, 5), Interval(7, 9)])
    print(res)
    res = merge_intervals([Interval(6, 7), Interval(2, 4), Interval(5, 9)])
    print(res)
    res = merge_intervals([Interval(1, 4), Interval(2, 6), Interval(3, 5)])
    print(res)

    res = any_overlap([Interval(1, 4), Interval(2, 5), Interval(7, 9)])
    print(res)

    res = insert_interval([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6))
    print(res)
    res = insert_interval([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 10))
    print(res)

    inter_a = [Interval(x, y) for x, y in [[1, 3], [5, 6], [7, 9]]]
    inter_b = [Interval(x, y) for x, y in [[2, 3], [5, 7]]]

    res = merge(inter_a=inter_a, inter_b=inter_b)
    print('interval intersection', res)

    inter_a = [Interval(x, y) for x, y in [[1, 3], [5, 7], [9, 12]]]
    inter_b = [Interval(x, y) for x, y in [[5, 10]]]

    res = merge(inter_a=inter_a, inter_b=inter_b)
    print('interval intersection', res)

    inter_a = [Interval(x, y) for x, y in [[1, 4], [2, 5], [7, 9]]]
    print('Can I attend all my meetings?', find_conflicting_appointments(inter_a))

    inter_a = [Interval(x, y) for x, y in [[6, 7], [2, 4], [8, 12]]]
    print('Can I attend all my meetings?', find_conflicting_appointments(inter_a))

    inter_a = [Interval(x, y) for x, y in [[4, 5], [2, 3], [3, 6]]]
    print('Can I attend all my meetings?', find_conflicting_appointments(inter_a))

    inter_a = [Interval(x, y) for x, y in [[4, 5], [2, 3], [3, 6]]]
    print('Can I attend all my meetings?', find_conflicting_appointments(inter_a))


main()
