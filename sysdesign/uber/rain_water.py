class Stack:
    def __init__(self):
        self.right = []

    def push(self, val):
        self.right.append(val)

    def pop(self):
        return self.right.pop()

    def __len__(self):
        return len(self.right)

    def is_empty(self):
        return len(self) == 0

    def peak(self):
        return self.right[-1]

    def __repr__(self):
        return str(self.right)


def trap_water(elevation_map):
    stack = Stack()

    for i in reversed(elevation_map[1:]):
        if len(stack) == 0 or stack.peak() <= i:
            stack.push(i)
        else:
            stack.push(stack.peak())

    left = elevation_map[0]
    results = [0]
    for i in range(1, len(elevation_map)):
        left = max(elevation_map[i - 1], left)
        min_h = min(left, stack.pop())
        if elevation_map[i] < min_h:
            results.append(min_h - elevation_map[i])
        else:
            results.append(0)

    return sum(results)


def main():
    print(trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trap_water([4, 2, 0, 3, 2, 5]))
    print(trap_water([1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]))


main()
