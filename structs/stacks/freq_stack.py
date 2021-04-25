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

        return value

    def __getitem__(self, item):
        if item == 'push':
            return lambda *x: self.push(*x)
        if item == 'pop':
            return lambda *x: self.pop(*x)


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
