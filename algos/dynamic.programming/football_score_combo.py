scores = [2, 3, 7]


def find_num_of_combos(a, b):
    total = 0

    def helper(a, b, i):
        nonlocal total
        if b == 0:
            total += 1
            return

        if i >= len(a):
            return

        if a[i] <= b:
            helper(a, b - a[i], i)
        helper(a, b, i + 1)

    helper(a, b, 0)
    return total


print(find_num_of_combos(scores, 12))


def print_m(m, t):
    print([i for i in range(t + 1)])

    for r in m:
        print(r)


def find_num_of_combos(scores, t):
    matrix = [[1] + [0] * t for _ in range(len(scores))]

    for i in range(len(scores)):
        for j in range(1, t + 1):
            without_this_play = matrix[i - 1][j] if i > 0 else 0
            with_this_play = matrix[i][j - scores[i]] if j >= scores[i] else 0
            matrix[i][j] = without_this_play + with_this_play

    return matrix[-1][-1]


print(find_num_of_combos(scores, 12))
