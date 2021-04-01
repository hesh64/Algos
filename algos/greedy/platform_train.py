"""
Implement a function that returns the minimum number of platforms that are required for
the train so that none of them waits.


A train will wait if the arrival time of one train overlaps with the
arrival time of the other. So, the problem is to find the minimum number of platforms,
so that if the trains have an overlapping arrival time, they do not collide.
"""

import heapq


# Using a heap
def find_platform_heap(arrival, departure):
    intervals = list(zip(arrival, departure))
    heap = []

    intervals.sort(key=lambda x: x[0])
    heapq.heappush(heap, intervals[0][1])
    max_num = 1
    for interval in intervals[1:]:
        if interval[0] > heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
        max_num = max(len(heap), max_num)

    return max_num


def find_platform(arrival, departure):
    arrival.sort()
    departure.sort()

    i, j = 1, 0
    platforms_needed = 1
    # you'll need at least one platform
    result = 1

    while i < len(arrival) and j < len(departure):
        if arrival[i] < departure[j]:
            platforms_needed += 1
            i += 1
            result = max(platforms_needed, result)
        else:
            platforms_needed -= 1
            j += 1

    return result


def main():
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]

    print(find_platform(arrival, departure))

    # arrival = [200, 210, 300, 320, 350, 500]
    # departure = [230, 240, 320, 430, 400, 520]
    #
    # print(find_platform(arrival, departure))


main()
