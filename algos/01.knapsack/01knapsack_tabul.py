def knapsack(p, w, c):
    n = len(p)

    if c <= 0 or n == 0 or len(w) != n:
        return 0

    dp = [[0 for _ in range(c + 1)] for _ in range(n)]

    for i in range(0, n):
        dp[i][0] = 0

    for cap in range(0, c + 1):
        if w[0] <= cap:
            dp[0][cap] = p[0]

    for i in range(1, n):
        for cap in range(1, c + 1):
            profit1, profit2 = 0, 0

            if w[i] <= cap:
                profit1 = p[i] + dp[i - 1][cap - w[i]]

            profit2 = dp[i - 1][cap]

            dp[i][cap] = max(profit1, profit2)

    return dp[n - 1][c]


def main():
    print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
