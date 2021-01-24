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


main()
