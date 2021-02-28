"""
Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find
the total number of distinct ways to make up that amount.
"""


# brute force
def coin_change(din, a):
    if len(din) == 0 or a <= 0:
        return 0

    return coin_rec(din, a, 0)


def coin_rec(din, a, i):
    if a == 0:
        return 1

    if a < 0 or i >= len(din):
        return 0

    p1 = 0
    if din[i] <= a:
        p1 = coin_rec(din, a - din[i], i)

    return p1 + coin_rec(din, a, i + 1)


# memo
def coin_change_memo(din, a):
    if len(din) == 0 or a <= 0:
        return 0

    dp = [[-1 for _ in range(a + 1)] for _ in range(len(din))]

    return coin_memo(dp, din, a, 0)


def coin_memo(dp, din, a, i):
    if a == 0:
        return 1

    if i >= len(din) or a < 0:
        return 0

    if dp[i][a] == -1:
        p1 = 0
        if din[i] <= a:
            p1 = coin_memo(dp, din, a - din[i], i)

        p2 = coin_memo(dp, din, a, i + 1)

        dp[i][a] = p1 + p2
    return dp[i][a]


def main():
    din, a = [1, 2, 3], 5
    result = coin_change(din, a)
    print(result)

    din, a = [1, 2, 3], 5
    result = coin_change_memo(din, a)
    print(result)


main()
