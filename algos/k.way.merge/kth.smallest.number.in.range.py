"""
Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.
"""

import math
from heapq import heappush, heappop


# Time Complexity O(n* log(m))
# Space is O(m)
def find_smallest_range(lists):
    min_heap = []
    range_start, range_end = 0, math.inf
    cur_max = -math.inf

    for array in lists:
        # push the first elements, idx, and array/row
        heappush(min_heap, (array[0], 0, array))
        # find the max from the 0 index of all the rows
        cur_max = max(cur_max, array[0])

    # this is what guarantees that we have an elements from each array
    # we push another elements into the heap every time an elements from the
    # same array leaves the heap.
    while len(min_heap) == len(lists):
        # pop a value
        num, i, array = heappop(min_heap)
        # if the initial values of range_end - range_start are larger than
        # the curr_max - num (num will be the min)
        # then go ahead and set them as range_start, and arange end
        if range_end - range_start > cur_max - num:
            range_start = num
            range_end = cur_max

        # is there another idx in that array?
        if len(array) - 1 > i:
            # then go ahead and push that elements into the heap
            heappush(min_heap, (array[i + 1], i + 1, array))
            # that could potentially change the current max in the heap
            cur_max = max(cur_max, array[i + 1])

    # return whatever go set.
    return [range_start, range_end]


def main():
    l1 = [1, 5, 8]
    l2 = [4, 12]
    l3 = [7, 8, 10]

    result = find_smallest_range([l1, l2, l3])
    print(result)


main()
