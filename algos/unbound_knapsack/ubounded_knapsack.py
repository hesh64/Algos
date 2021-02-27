def knapsack(p, w, c):
    if len(p) == 0:
        return 0

    return knapsack_rec(p, w, c, 0)


def knapsack_rec(p, w, c, i):
    if c == 0 or i >= len(p):
        return 0

    profit1 = 0
    if w[i] <= c:
        profit1 = p[i] + knapsack_rec(p, w, c - w[i], i)

    profit2 = knapsack_rec(p, w, c, i + 1)

    return max(profit1, profit2)


def knapsack_memo(p, w, c):
    if len(p) == 0 or c <= 0:
        return 0

    dp = [[-1 for _ in range(c + 1)] for _ in range(len(p))]
    return knapsack_memo_rec(dp, p, w, c, 0)


def knapsack_memo_rec(dp, p, w, c, i):
    if c <= 0 or len(p) <= i:
        return 0

    if dp[i][c] == -1:
        profit1 = 0
        if w[i] <= c:
            profit1 = p[i] + knapsack_memo_rec(dp, p, w, c - w[i], i)

        profit2 = knapsack_memo_rec(dp, p, w, c, i + 1)
        dp[i][c] = max(profit1, profit2)

    return dp[i][c]


def knapsack_tabul(p, w, c):
    if len(p) == 0 or c <= 0 or len(w) != len(p):
        return 0

    n = len(p)
    dp = [[0 for _ in range(c + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for j in range(1, c + 1):
            profit1, profit2 = 0, 0
            if w[i] <= j:
                profit1 = p[i] + dp[i][j - w[i]]
            if i > 0:
                profit2 = dp[i - 1][j]
            dp[i][j] = max(profit1, profit2)

    for r in dp:
        print(r)

    return dp[n - 1][c]


def main():
    p = [15, 20, 50]
    w = [1, 2, 3]
    c = 5
    result = knapsack(p, w, c)
    print(result)

    p = [15, 20, 50]
    w = [1, 2, 3]
    c = 5
    result = knapsack_memo(p, w, c)
    print(result)

    p = [15, 50, 60, 90]
    w = [1, 3, 4, 5]
    c = 8
    result = knapsack_tabul(p, w, c)
    print(result)


main()
