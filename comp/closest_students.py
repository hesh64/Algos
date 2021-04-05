"""
group points to their closest neighbors
"""


def points(n, cords):
    taken = set()
    stack = []

    min_avg = float('inf')
    min_set = []

    def dist(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** .5

    def helper(n, cords, stack, taken):
        nonlocal min_avg, min_set
        if n == 0:
            if sum(stack) / len(stack) < min_avg:
                min_avg = sum(stack) / len(stack)
                min_set = stack.copy()
                return

        for i in range(len(cords)):
            for j in range(len(cords)):
                if i != j and i not in taken and j not in taken:
                    print(cords[i], cords[j])
                    stack.append(dist(cords[i], cords[j]))
                    taken.add(i)
                    taken.add(j)
                    helper(n - 1, cords, stack, taken)

                    taken.remove(i)
                    taken.remove(j)
                    stack.pop()

    helper(n, cords, stack, taken)
    return min_avg, min_set


if __name__ == '__main__':
    r = points(2, [[1, 1], [8, 6], [6, 8], [1, 3]])
    print(r)
