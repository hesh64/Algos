"""
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.
"""

from heapq import *


# time O(n*log(n))
# space O(n)
def sum_between_kth_kth(nums, k1, k2):
    min_heap = []

    # O(n log(n))
    for num in nums:
        heappush(min_heap, num)

    # k1 < n * log(n)
    for _ in range(k1):
        heappop(min_heap)

    # k2 - k1 < n * log(n)
    sum_ = 0
    for _ in range(k2 - k1 - 1):
        sum_ += heappop(min_heap)

    return sum_


"""but we can do better"""


# time is O(n * log(k2))
# space is O(k2)
def find_sum_of_elements(nums, k1, k2):
    min_heap = []

    # n * log(k2)
    for i in range(len(nums)):
        if i < k2 - 1:
            heappush(min_heap, -nums[i])
        elif nums[i] < -min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, -nums[i])

    sum_ = 0
    for _ in range(k2 - k1 - 1):
        sum_ += -heappop(min_heap)
    return sum_


def main():
    nums, k1, k2 = [1, 3, 12, 5, 15, 11], 3, 6
    result = sum_between_kth_kth(nums, k1, k2)
    print(result)

    nums, k1, k2 = [1, 3, 12, 5, 15, 11], 3, 6
    result = find_sum_of_elements(nums, k1, k2)
    print(result)


main()
