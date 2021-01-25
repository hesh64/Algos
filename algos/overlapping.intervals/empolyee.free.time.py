class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start


    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"


def find_employee_free_time(schedules):
    merged = []

    for schedule in schedules:
        merged.extend(schedule)

    merged.sort(key=lambda x: x.start)

    start, end = merged[0].start, merged[0].end

    new_schedule = []
    free_time = []
    for i in range(1, len(merged)):
        interval = merged[i]

        if start <= interval.start <= end:
            end = max(end, interval.end)
        else:
            new_interval = Interval(start, end)
            if len(new_schedule):
                free_time.append(Interval(new_schedule[-1].end, new_interval.start))
            new_schedule.append(new_interval)
            start = interval.start
            end = interval.end

    new_interval = Interval(start, end)
    if len(new_schedule):
        free_time.append(Interval(new_schedule[-1].end, new_interval.start))
    new_schedule.append(new_interval)

    return free_time

def find_employee_free_time2(schedules):
    merged = []

    for schedule in schedules:
        merged.extend(schedule)

    merged.sort(key=lambda x: x.start)

    start, end = merged[0].start, merged[0].end

    new_schedule = []
    free_time = []
    for i in range(1, len(merged)):
        interval = merged[i]

        if start <= interval.start <= end:
            end = max(end, interval.end)
        else:
            new_interval = Interval(start, end)
            if len(new_schedule):
                free_time.append(Interval(new_schedule[-1].end, new_interval.start))
            new_schedule.append(new_interval)
            start = interval.start
            end = interval.end

    new_interval = Interval(start, end)
    if len(new_schedule):
        free_time.append(Interval(new_schedule[-1].end, new_interval.start))
    new_schedule.append(new_interval)

    return free_time


def main():
    schedule = [
        [Interval(start, end) for start, end in [[1, 3], [9, 12]]],
        [Interval(start, end) for start, end in [[2, 4]]],
        [Interval(start, end) for start, end in [[6, 8]]]
    ]

    result = find_employee_free_time(schedule)

    print(result)


main()
