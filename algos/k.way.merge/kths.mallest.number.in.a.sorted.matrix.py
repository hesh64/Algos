"""
Given an N * NN∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.
"""

from heapq import *


def kth_smallest_number(matrix, k):
    m = len(matrix)
    row = (k % m) - 1
    col = k // m

    return matrix[row][col]


# that way too easy let's do it the k way.....

def kth_smallest_num_in_matrix(matrix, k):
    min_heap = []

    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))

    count, number = 0, 0
    while min_heap:
        number, idx, row = heappop(min_heap)
        count += 1

        if count == k:
            break

        if len(row) > idx + 1:
            heappush(min_heap, (row[idx + 1], idx + 1, row))

    return number


def main():
    matrix = [
        [2, 6, 8],
        [3, 7, 10],
        [5, 8, 11],
    ]
    k = 5
    result = kth_smallest_number(matrix, k)
    print(result)

    matrix = [
        [2, 6, 8],
        [3, 7, 10],
        [5, 8, 11],
    ]
    k = 5
    result = kth_smallest_num_in_matrix(matrix, k)
    print(result)


main()
