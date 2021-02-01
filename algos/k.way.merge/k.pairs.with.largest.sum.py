"""
Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of
numbers from both the arrays.

"""
from heapq import heappush, heappop

"""
Since, at most, we’ll be going through all the elements of both arrays and we will add/remove one element in the heap 
in each step, the time complexity of the above algorithm will be O(n * m *logK) where ‘N’ and ‘M’ are the total 
number of elements in both arrays, respectively.

If we assume that both arrays have at least ‘K’ elements then the time complexity can be simplified to O(k^2 * log(k))
 because we are not iterating more than ‘K’ elements in both arrays.
"""


def k_largest_sum_pairs(l1, l2, k):
    min_heap = []

    for i in range(min(k, len(l1))):
        for j in range(min(k, len(l2))):
            if len(min_heap) < k:
                heappush(min_heap, ((l1[i] + l2[j]), i, j))
            else:
                if l1[i] + l2[j] < min_heap[0][0]:
                    break
                else:
                    heappop(min_heap)
                    heappush(min_heap, (l1[i] + l2[j], i, j))

    return [[l1[t[1]], l2[t[2]]] for t in min_heap]


def main():
    l1 = [9, 8, 2]
    l2 = [6, 3, 1]
    k = 3

    result = k_largest_sum_pairs(l1, l2, k)
    print(result)


main()
