import random

random.seed(100)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)

    def getMax(self):
        if self.heap:
            return self.heap[0]

        return None

    def removeMax(self):
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max

        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max

        else:
            return None

    def __percolateUp(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return

        if self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.__percolateUp(parent)

    def __maxHeapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if len(self.heap) > left and self.heap[left] > self.heap[largest]:
            largest = left

        if len(self.heap) > right and self.heap[right] > self.heap[largest]:
            largest = right

        if index != largest:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.__maxHeapify(largest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.__maxHeapify(i)


def main():
    heap = MaxHeap()

    for _ in range(10):
        heap.insert(random.randint(0, 100))

    for _ in range(10):
        print(heap.removeMax())


main()
