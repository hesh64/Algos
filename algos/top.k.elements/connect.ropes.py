"""
Connect Ropes

Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost.
The cost of connecting two ropes is equal to the sum of their lengths.
"""
from heapq import *


def connect_ropes(ropes):
    min_heap = []

    for r in ropes:
        heappush(min_heap, r)

    result, temp = 0, 0
    while len(min_heap) > 1:
        temp = heappop(min_heap) + heappop(min_heap)
        result += temp
        heappush(min_heap, temp)

    return result


def main():
    result = connect_ropes([1, 3, 11, 5])
    print(result)

    result = connect_ropes([3, 4, 5, 6])
    print(result)


main()
