"""

Introduction
Any problem that asks us to find the top/smallest/frequent ‘K’ elements among a given set falls under this pattern.

The best data structure that comes to mind to keep track of ‘K’ elements is Heap. This pattern will make use of the Heap
to solve multiple problems dealing with ‘K’ elements at a time from a set of given elements.

Let’s jump onto our first problem to develop an understanding of this pattern.


"""

from heapq import *

"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.
"""


# time complexity here is hard: O(k*log(k) + (N - K) * log(k))
# space O(k)
def top_k_largest(nums, k):
    min_heap = []
    for num in nums:
        if len(min_heap) >= k:
            if num > min_heap[0]:
                heappushpop(min_heap, num)
        else:
            heappush(min_heap, num)

    return min_heap


"""
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.
"""


# time complexity here is hard: O(k*log(k) + (N - K) * log(k)) which equal O(n * log(k))
# space O(k)
def top_k_smallest(nums, k):
    min_heap = []
    for num in nums:
        if len(min_heap) >= k:
            if num > min_heap[0]:
                heappushpop(min_heap, -num)
        else:
            heappush(min_heap, -num)

    return -min_heap[0]


def k_closest_point_to_the_origin(points, k):
    sqrt_map = {}

    def dist(x, y):
        nonlocal sqrt_map
        sq = (x ** 2 + y ** 2) ** .5

        if sq not in min_heap:
            sqrt_map[str(sq)] = [x, y]

        return sq

    min_heap = []

    for i in range(k):
        heappush(min_heap, -dist(*points[i]))

    for i in range(k, len(points)):
        sq = -dist(*points[i])
        if sq > min_heap[0]:
            val = heappushpop(min_heap, sq)
            del sqrt_map[str(-val)]

    return [sqrt_map[str(-i)] for i in min_heap]


def main():
    nums, k = [3, 1, 5, 12, 2, 11], 3
    result = top_k_largest(nums, k)
    print(result)

    nums, k = [5, 12, 11, -1, 12], 3
    result = top_k_largest(nums, k)
    print(result)

    nums, k = [1, 5, 12, 2, 11, 5], 3
    result = top_k_smallest(nums, k)
    print(result)

    nums, k = [1, 5, 12, 2, 11, 5], 4
    result = top_k_smallest(nums, k)
    print(result)

    nums, k = [5, 12, 11, -1, 12], 3
    result = top_k_smallest(nums, k)
    print(result)

    points, k = [[1, 2], [1, 3]], 1
    result = k_closest_point_to_the_origin(points, k)
    print(result)

    points, k = [[1, 3], [3, 4], [2, -1]], 2
    result = k_closest_point_to_the_origin(points, k)
    print(result)


main()
