"""
count the number of ways to choose k things from n
n!/((n-k)!k!) -> (n - 1) choose (k - 1) + (n - 1) choose (k)

"""


# O(n^2) time O(n^2) space
def binomial_coefficient(n, k):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n + 1):
        dp[i][0] = 1

    for j in range(n + 1):
        dp[j][j] = 1

    for i in range(1, n + 1):
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    for r in dp:
        print(r)
    return dp[n][k]
    # return dp


# O(n^2) time O(n) space
def binomial_coefficient_opt(n, k):
    dp = [1]

    for i in range(1, n + 1):
        new_dp = [1] * (i + 1)
        for j in range(len(new_dp) - 1, 0, -1):
            new_dp[j] = (dp[j] if j < len(dp) else 0) + dp[j - 1]
        dp = new_dp

    return dp[k]


print(binomial_coefficient(5, 4))
print(binomial_coefficient(5, 3))
print(binomial_coefficient_opt(5, 3))
