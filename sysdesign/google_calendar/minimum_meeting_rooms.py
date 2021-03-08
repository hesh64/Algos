from heapq import heappush, heappop


def minimum_meeting_rooms(meeting_times):
    meeting_times.sort(key=lambda x: x[0])
    heap = []
    heappush(heap, meeting_times[0][1])
    for i in meeting_times[1:]:
        if heap[0] <= i[0]:
            heappop(heap)
        heappush(heap, i[1])

    return len(heap)


def main():
    meeting_times = [[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]]
    min_rooms = minimum_meeting_rooms(meeting_times)
    print(min_rooms)


main()
