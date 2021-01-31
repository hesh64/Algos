from heapq import *


class FreqTuple:
    def __init__(self, val, freq):
        self.val, self.freq = val, freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __repr__(self):
        return f'{self.val}'


def top_k_frequent(nums, _k):
    min_heap = []
    freq = {}

    # O(n)
    for n in nums:
        if n not in freq:
            freq[n] = 0
        freq[n] += 1

    # O(n * log(k))
    for (k, v) in freq.items():
        tup = FreqTuple(k, v)
        if len(min_heap) < _k:
            heappush(min_heap, tup)
        else:
            if tup > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, tup)

    return list(min_heap)


def main():
    array, k = [1, 3, 5, 12, 11, 12, 11], 2
    result = top_k_frequent(array, k)
    print(result)

    array, k = [5, 12, 11, 3, 11], 2
    result = top_k_frequent(array, k)
    print(result)


main()
