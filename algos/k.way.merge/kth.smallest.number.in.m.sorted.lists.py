"""
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.
"""

from heapq import *


# O(k * log(m))
# O(m)
def kth_smallest_number_in_m_sorted_lists(lists, k):
    max_heap = []
    # use an array it's cheaper
    # store this in the tuple instead of a separate object
    idxes = {}
    heap_count = 0
    # o(m)
    for i in range(len(lists)):
        idxes[i] = 0
        heappush(max_heap, (-lists[i][idxes[i]], i))
        idxes[i] += 1
        heap_count += 1

        if heap_count == k:
            return max_heap[0]

    # will at the most, run k times
    while heap_count <= k:
        value, index = heappop(max_heap)

        if len(lists[index]) - 1 > idxes[index]:
            idxes[index] += 1
            # log(m) because each array has at most 1 elements in the heap
            heappush(max_heap, (-lists[index][idxes[index]], index))
            heap_count += 1
    # o(m)
    while len(max_heap) > 1:
        heappop(max_heap)

    # return the - of the -
    return -max_heap[0][0]


def main():
    l1 = [2, 6, 8]
    l2 = [3, 6, 7]
    l3 = [1, 3, 4]
    lists, k = [l1, l2, l3], 5

    result = kth_smallest_number_in_m_sorted_lists(lists, k)
    print(result)


main()
