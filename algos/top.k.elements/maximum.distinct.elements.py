"""
Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left
with maximum distinct numbers.
"""

from heapq import *


# O(k*log(n) + n*log(n))
def max_distinct_k(nums, k):
    distinct_count = 0
    # the scenario where k is as large as nums
    if len(nums) <= k:
        return distinct_count

    frequency = {}

    # get the frequencies
    # O(n)
    for num in nums:
        if num not in frequency:
            frequency[num] = 0
        frequency[num] += 1

    # either count the distinct elements or push into
    # the heap
    min_heap = []
    # worst case it's O((1/2)n * log(k)) => nlog(k)
    for (num, freq) in frequency.items():
        if freq == 1:
            distinct_count += 1
        else:
            heappush(min_heap, (freq, num))

    # while we can remove items from the heap and heap
    # length is not 0
    # worst case this is k *log(n)
    while k > 0 and min_heap:
        # pop a num and it's frequency
        freq, num = heappop(min_heap)
        # freq -1 accounts for a single occurance of that element
        k -= freq - 1
        # did removing the extras keep k larger than or eq to 0
        # great so we have another distinct element
        if k >= 0:
            distinct_count += 1

    # wow k still has more milleage?
    if k > 0:
        # gotta subtract those extra miles from the distinct values because
        # we still need to remove k elements.
        distinct_count -= k

    # return the count.
    return distinct_count


def main():
    nums, k = [7, 3, 5, 8, 5, 3, 3], 2
    result = max_distinct_k(nums, k)
    print(result)


main()
