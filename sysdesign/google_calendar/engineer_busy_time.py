# O(nlog(n)) Time and O(n) space
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    start, end = intervals[0]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if end >= interval[0]:
            end = max(end, interval[1])
        else:
            merged.append([start, end])
            start, end = interval
    merged.append([start, end])
    return merged


def main():
    meeting_times = [[1, 4], [2, 5], [6, 8], [7, 9], [10, 13]]
    print(merge_intervals(meeting_times))

    meeting_times = [[4, 7], [1, 3], [8, 10], [2, 3], [6, 8]]
    print(merge_intervals(meeting_times))


main()
