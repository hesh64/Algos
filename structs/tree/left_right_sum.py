def sum_subtrees(a):
    if len(a) == 0:
        return 0

    left_sum, right_sum = 0, 0
    pos = pow = 1

    while True:
        start = pos
        end = start + 2 ** pow
        break_after_this = end >= len(a)
        end = min(len(a), end)

        for i in range(start, min(start + (2 ** pow) // 2, len(a))):
            if a[i] != -1:
                left_sum += a[i]

        for j in range(min(start + (2 ** pow) // 2, len(a)), end):
            if a[j] != -1:
                right_sum += a[j]

        if break_after_this:
            break

        pos += 2 ** pow
        pow += 1

    return left_sum, right_sum


print(sum_subtrees([3, 6, 7, 5, 2, -1, 1]))
print(sum_subtrees([3, 6, 7, 5, 2, -1, 1, 2, 3, 4, 5, -1, -1, 0, 1]))
