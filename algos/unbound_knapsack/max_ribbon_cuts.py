"""
We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. We need to cut the ribbon
into the maximum number of pieces that comply with the above-mentioned possible lengths. Write a method that will
return the count of pieces.
"""


def max_ribbons(lengths, n):
    if len(lengths) == 0 or n <= 0:
        return 0

    return max_ribbons_rec(lengths, n, 0, 0)


def max_ribbons_rec(lengths, n, i, c):
    if n == 0:
        return c

    if n < 0 or i >= len(lengths):
        return 0

    p1 = 0
    if lengths[i] <= n:
        p1 = max_ribbons_rec(lengths, n - lengths[i], i, c + 1)
    p2 = max_ribbons_rec(lengths, n, i + 1, c)
    return max(p1, p2)


def max_ribbons_memo(lengths, n):
    if len(lengths) == 0 or n <= 0:
        return 0

    dp = [[-1 for _ in range(n + 1)] for _ in range(len(lengths))]
    return max_ribbon_rec_memo(dp, lengths, n, 0, 0)


def max_ribbon_rec_memo(dp, lengths, n, i, c):
    if n == 0:
        return c

    if n < 0 or len(lengths) <= i:
        return 0

    if dp[i][n] == -1:
        p1 = 0
        if lengths[i] <= n:
            p1 = max_ribbon_rec_memo(dp, lengths, n - lengths[i], i, c + 1)
        p2 = max_ribbon_rec_memo(dp, lengths, n, i + 1, c)

        dp[i][n] = max(p1, p2)
    return dp[i][n]


def main():
    arr, n = [2, 3], 5
    result = max_ribbons(arr, n)
    print(result)
    arr, n = [2, 3], 7
    result = max_ribbons(arr, n)
    print(result)
    arr, n = [3, 5, 7], 13
    result = max_ribbons(arr, n)
    print(result)

    print('\nmemo')
    arr, n = [2, 3], 5
    result = max_ribbons_memo(arr, n)
    print(result)
    arr, n = [2, 3], 7
    result = max_ribbons_memo(arr, n)
    print(result)
    arr, n = [3, 5, 7], 13
    result = max_ribbons_memo(arr, n)
    print(result)


main()
