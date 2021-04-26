import random

random.seed(0)


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__rollUp(len(self.heap) - 1)

    def getMin(self):
        if len(self.heap):
            return self.heap[0]
        return None

    def removeMin(self):
        if len(self.heap) == 1:
            tmp = self.heap[0]
            del self.heap[0]
            return tmp

        elif len(self.heap) > 1:
            tmp = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__heapify(0)
            return tmp

        return None

    def __rollUp(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return

        if self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.__rollUp(parent)

    def __heapify(self, index):
        left = (2 * index) + 1
        right = (2 * index) + 2

        smallest = index

        if len(self.heap) > left and self.heap[index] > self.heap[left]:
            smallest = left

        if len(self.heap) > right and self.heap[index] > self.heap[right]:
            smallest = right

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.__heapify(smallest)


def main():
    heap = MinHeap()

    for _ in range(10):
        heap.insert(random.randint(0, 100))

    for _ in range(10):
        print(heap.removeMin())


main()
