"""
Given a set of positive numbers, find the total number of subsets
whose sum is equal to a given number ‘S’.

"""


def count_subset_sum(nums, s):
    if s <= 0 or len(nums) == 0:
        return 0

    return count(nums, s, 0)


def count(nums, s, i):
    if s == 0:
        return 1

    if i >= len(nums):
        return 0

    p1 = 0
    if nums[i] <= s:
        p1 = count(nums, s - nums[i], i + 1)

    return p1 + count(nums, s, i + 1)


def count_subset_sum_memo(nums, s):
    if s <= 0 or len(nums) == 0:
        return 0

    dp = [[False for _ in range(s + 1)] for _ in range(len(nums))]
    return count_memo(dp, nums, s, 0)


def count_memo(dp, nums, s, i):
    if s == 0:
        return 1

    if i >= len(nums):
        return 0

    if dp[i][s] is False:
        p1 = 0
        if nums[i] <= s:
            p1 = count_memo(dp, nums, s - nums[i], i + 1)

        p2 = count_memo(dp, nums, s, i + 1)
        dp[i][s] = p1 + p2

    return dp[i][s]


# todo there is a bug in here the count is off by 1
def count_subset_tabul(nums, s):
    if len(nums) == 0 or s <= 0:
        return 0

    n = len(nums)
    dp = [[-1 for _ in range(s + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for j in range(s + 1):
        dp[0][j] = 1 if j == nums[0] else 0

    for i in range(1, n):
        for j in range(1, s + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i]:
                dp[i][j] += dp[i - 1][j - nums[i]]

    return dp[n - 1][s]


def main():
    print('brute')
    set, s = [1, 1, 2, 3], 4
    result = count_subset_sum(set, s)
    print(result)
    set, s = [1, 2, 7, 1, 5], 9
    result = count_subset_sum(set, s)
    print(result)

    print('\nmemo')
    set, s = [1, 1, 2, 3], 4
    result = count_subset_sum_memo(set, s)
    print(result)
    set, s = [1, 2, 7, 1, 5], 9
    result = count_subset_sum_memo(set, s)
    print(result)

    print('\ntabul')
    set, s = [1, 1, 2, 3], 4
    result = count_subset_tabul(set, s)
    print(result)
    set, s = [1, 2, 7, 1, 5], 9
    result = count_subset_tabul(set, s)
    print(result)


main()
