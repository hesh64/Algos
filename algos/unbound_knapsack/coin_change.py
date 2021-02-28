import math

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


# O(T * C) C is len(denominations) T = total
def coin_change_tabul(denominations, total):
    if len(denominations) == 0 or total <= 0:
        return 0

    n = len(denominations)
    dp = [[0 for _ in range(total + 1)] for _ in range(n)]

    # the 0 total set
    for i in range(n):
        dp[i][0] = 1

    for i in range(n):
        for t in range(1, total + 1):
            # if there is a previous row
            if i > 0:
                # grab the value calculated for this position
                # from the previous row.
                dp[i][t] = dp[i - 1][t]
            # if value of s is larger than denominations[i] -> this means
            # that to compose s we need, denomination[i] + another coin
            # the way we calculate it is by subtracting the current denomination[i]
            # from t, to get the left over piece to construct s
            if t >= denominations[i]:
                dp[i][t] += dp[i][t - denominations[i]]

    return dp[n - 1][total]


"""
Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked 
to find the minimum number of coins needed to make up that amount.
"""


def minimum_coin_change(denominations, total):
    if len(denominations) == 0 or total <= 0:
        return 0

    return min_coins(denominations, total, 0, 0)


def min_coins(denominations, total, i, c):
    if total == 0:
        return c
    if total < 0 or i >= len(denominations):
        return math.inf

    if denominations[i] <= total:
        return min(min_coins(denominations, total - denominations[i], i, c + 1),
                   min_coins(denominations, total, i + 1, c))

    return min_coins(denominations, total, i + 1, c)


# todo there is a bug in here
def minimum_coin_change_memo(denomination, total):
    if len(denomination) == 0 or total <= 0:
        return 0

    dp = [[-1 for _ in range(total + 1)] for _ in range(len(denomination))]
    return min_coins_memo(dp, denomination, total, 0, 0)


def min_coins_memo(dp, denomination, total, i, c):
    if total == 0:
        return c
    if i >= len(denomination) or total < 0:
        return math.inf

    if dp[i][total] == -1:
        p1 = math.inf
        if denomination[i] <= total:
            p1 = min_coins_memo(dp, denomination, total - denomination[i], i, c + 1),

        dp[i][total] = min(p1, min_coins_memo(dp, denomination, total, i + 1, c))
    return dp[i][total]


def main():
    print('brute')
    din, a = [1, 2, 3], 5
    result = coin_change(din, a)
    print(result)

    print('\nmemo')
    din, a = [1, 2, 3], 5
    result = coin_change_memo(din, a)
    print(result)

    print('\ntabul')
    result = coin_change_tabul([1, 2, 3], 5)
    print(result)

    print('\n\nfind minimum coins')
    print('brute')
    deno, s = [1, 2, 3], 5
    print(minimum_coin_change(deno, s))
    deno, s = [1, 2, 3], 7
    print(minimum_coin_change(deno, s))
    deno, s = [1, 2, 3], 11
    print(minimum_coin_change(deno, s))
    print('\nmemo')
    deno, s = [1, 2, 3], 5
    print(minimum_coin_change_memo(deno, s))
    deno, s = [1, 2, 3], 7
    print(minimum_coin_change_memo(deno, s))
    deno, s = [1, 2, 3], 11
    print(minimum_coin_change_memo(deno, s))


main()
