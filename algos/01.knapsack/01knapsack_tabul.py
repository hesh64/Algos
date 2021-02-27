def knapsack(profits, weights, capacity):
    if len(profits) == 0 or capacity <= 0 or len(profits) != len(weights):
        return 0

    n = len(profits)

    # we want to generate a table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]
    # this is to deal with the one weight case.
    # we will take it as long as it's not more than the cpaacity
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for row in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            if weights[row] <= c:
                profit1 = profits[row] + dp[row - 1][c - weights[row]]

            profit2 = dp[row - 1][c]

            dp[row][c] = max(profit1, profit2)

    return dp[n - 1][capacity]
    # print('max profit is', dp[n - 1][capacity])

    # finalp = dp[n - 1][capacity]
    # i = n - 1
    # c = capacity
    # lst = []
    # while finalp > 0 and i > -1 and c > 0:
    #     if finalp == dp[i - 1][c]:
    #         i -= 1
    #
    #     else:
    #         lst.append(profits[i])
    #         finalp -= profits[i]
    #         for id in range(1, capacity):
    #             if dp[i][id] == finalp:
    #                 c = id
    #
    # return lst


def main():
    print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
