"""
Problem Statement #
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of
the middle two numbers.


we can do a brute force method:
maintain a full list of items, and insert items into it at their correct order
that's insertion sort - O(n)

another approach would be to use 2 heaps

heap 1 - min heap with all the large elements
heap 2 - max heap with all the small elements

the median would be the sweet spot between the two

[4, 5, 6, 7] [3, 2 1, 0]

insertions here will cost O(log(n))


We can insert a number in the Max Heap (i.e. first half) if the number is smaller than
the top (largest) number of the heap. After every insertion, we will balance the number of elements
in both heaps, so that they have an equal number of elements.
If the count of numbers is odd, let’s decide to have more numbers in max-heap than the Min Heap.


this assumes numbers >= 0

i belive we can apply this to negatives IF we know the smallest negative and shift all numbers by
the absolute value of it
"""

from heapq import *


class MedianOfAStream:
    max_heap = []
    min_heap = []

    # we will push into max_heap first
    # O(log(n))
    def insert(self, num):
        if not self.max_heap or self.max_heap[0] >= -num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) + 1 < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    # two possible cases
    # min and max are same length so we average their heads
    # max is longer so we return it's head
    # O(1)
    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

        else:
            return (-self.max_heap[0]) / 1.0


def main():
    median = MedianOfAStream()
    median.insert(3)
    median.insert(1)
    print(median.find_median())
    median.insert(5)
    print(median.find_median())
    median.insert(4)
    print(median.find_median())


main()
