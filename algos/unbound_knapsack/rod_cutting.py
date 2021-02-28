"""
Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that
will maximize the profit. We are also given the price of every piece of length ‘i’
where ‘1 <= i <= n’.

Example:

Lengths: [1, 2, 3, 4, 5]
Prices: [2, 6, 7, 10, 13]
Rod Length: 5

Let’s try different combinations of cutting the rod:

Five pieces of length 1 => 10 price
Two pieces of length 2 and one piece of length 1 => 14 price
One piece of length 3 and two pieces of length 1 => 11 price
One piece of length 3 and one piece of length 2 => 13 price
One piece of length 4 and one piece of length 1 => 12 price
One piece of length 5 => 13 price

This shows that we get the maximum price (14) by cutting the rod into two pieces of length ‘2’ and one
piece of length ‘1’.
"""


def rod_cutting(lengths, prices, length):
    if len(lengths) == 0 or length == 0 or len(prices) == 0:
        return 0

    return rot_cutting_rec(lengths, prices, length, 0, 0)


def rot_cutting_rec(lengths, prices, length, index, profits):
    if index >= len(lengths) or length == 0:
        return profits

    profit1 = 0

    if lengths[index] <= length:
        profit1 = rot_cutting_rec(lengths, prices, length - lengths[index], index, profits + prices[index])

    profit2 = rot_cutting_rec(lengths, prices, length, index + 1, profits)

    return max(profit1, profit2)


def rod_cutting_memo(p, ls, l):
    if len(p) == 0 or len(p) != len(ls) or l <= 0:
        return 0

    dp = [[-1 for _ in range(l + 1)] for _ in range(len(p))]
    return rod_cut_memo(dp, p, ls, l, 0)


def rod_cut_memo(dp, p, ls, l, i):
    if l <= 0 or i >= len(p):
        return 0

    if dp[i][l] == -1:
        p1 = 0
        if ls[i] <= l:
            p1 = p[i] + rod_cut_memo(dp, p, ls, l - ls[i], i)
        dp[i][l] = max(p1, rod_cut_memo(dp, p, ls, l, i + 1))
    return dp[i][l]


def rod_cut_tabul(p, ls, l):
    if len(p) != len(ls) or len(ls) == 0 or l <= 0:
        return 0
    n = len(p)
    dp = [[0 for _ in range(l + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for j in range(1, l + 1):
        if j % ls[0] == 0:
            dp[0][j] = (j // ls[0]) * p[0]

    for i in range(1, n):
        for j in range(1, l + 1):
            p1, p2 = 0, 0
            if ls[i] <= j:
                p1 = p[i] + dp[i][j - ls[i]]
            if i > 0:
                p2 = dp[i - 1][j]
            dp[i][j] = max(p1, p2)

    for r in dp:
        print(r)
    return dp[n - 1][l]


def main():
    lengths = [1, 2, 3, 4, 5]
    prices = [2, 6, 7, 10, 13]
    length = 5

    result = rod_cutting(lengths, prices, length)
    print(result)

    lengths = [1, 2, 3, 4, 5]
    prices = [2, 6, 7, 10, 13]
    length = 5
    result = rod_cutting_memo(prices, lengths, length)
    print(result)

    lengths = [1, 2, 3, 4, 5]
    prices = [2, 6, 7, 10, 13]
    length = 5
    result = rod_cut_tabul(prices, lengths, length)
    print(result)


main()
