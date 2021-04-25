import heapq
from collections import defaultdict


class Freq:
    def __init__(self):
        self.counter = 0
        self.stacks = defaultdict(list)
        self.max_freqs = {}
        self.max_index = 0

    def __add_at_index(self, i, value):
        self.stacks[i].append(value)
        self.max_index = max(i, self.max_index)

    def __red_freq(self, value):
        self.max_freqs[value] -= 1
        if self.max_freqs[value] == 0:
            del self.max_freqs[value]

    def push(self, value):
        if value not in self.max_freqs:
            self.max_freqs[value] = 1
            self.__add_at_index(1, value)
            return

        self.max_freqs[value] += 1
        self.__add_at_index(self.max_freqs[value], value)

    def pop(self):
        if self.max_index == 0:
            return None

        value = self.stacks[self.max_index].pop()
        self.__red_freq(value)

        if len(self.stacks[self.max_index]) == 0:
            del self.stacks[self.max_index]
            self.max_index -= 1

# there is a bug in this implementation
# class HeapNode:
#     counter = 0
#
#     def __init__(self, value):
#         self.value = value
#         HeapNode.counter += 1
#         self.counter = HeapNode.counter
#         self.freq = 1
#
#     def __lt__(self, other):
#         return self.freq > other.freq or \
#                (self.freq == other.freq and self.counter > other.counter)
#
#     def __repr__(self):
#         return f'(value={self.value}, freq={self.freq}, counter={self.counter})'
#
#
# class Freq:
#     def __init__(self):
#         self.cache = {}
#         self.heap = []
#
#     def push(self, value):
#         if value not in self.cache:
#             self.cache[value] = HeapNode(value)
#             heapq.heappush(self.heap, self.cache[value])
#             return
#         self.cache[value].freq += 1
#         heapq.heapify(self.heap)
#
#     def pop(self):
#         print(self.heap)
#         if len(self.heap) == 0:
#             return None
#
#         top = heapq.heappop(self.heap)
#         top.freq -= 1
#         heapq.heappush(self.heap, top)
#         return top.value
#

def main():
    f = Freq()
    for i in [5, 7, 5, 7, 4, 5]:
        f.push(i)

    print(f.stacks)
    print([f.pop() for i in range(4)])

    f = Freq()
    l1 = ["push", "push", "push", "push", "push", "push", "pop", "push", "pop", "push", "pop", "push", "pop", "push",
          "pop",
          "pop", "pop", "pop", "pop", "pop"]
    l2 = [[4], [0], [9], [3], [4], [2], [], [6], [], [1], [], [1], [], [4], [], [], [], [], [], []]
    for fn, args in zip(l1, l2):
        print(f.stacks)
        print(f[fn](*args))

main()
