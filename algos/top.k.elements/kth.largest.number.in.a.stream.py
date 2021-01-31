"""

Design a class to efficiently find the Kth largest element in a stream of numbers.

The class should have the following two things:

1. The constructor of the class should accept an integer array containing initial numbers from the stream and an integer
 ‘K’.
2. The class should expose a function add(int num) which will store the given number and return the Kth largest number.
"""

from heapq import *


# time - insert costs O(log(k)) where k is size of heap
# starting the object may cost n log(k) where n is the size of nums
# space complexity is O(k) where k is the length of the heap
class KthLargest:
    def __init__(self, nums, k):
        self.k = k
        self.max_heap = []
        for num in nums:
            self.add(num)

    def add(self, number):
        heappush(self.max_heap, number)
        if len(self.max_heap) > self.k:
            heappop(self.max_heap)

        return self.max_heap[0]


def main():
    nums, k = [3, 1, 5, 12, 2, 11], 4
    kth = KthLargest(nums, k)
    print('1. calling add(6)', kth.add(6))
    print('2. calling add(13)', kth.add(13))
    print('3. calling add(4)', kth.add(4))


main()
