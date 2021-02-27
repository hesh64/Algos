"""
Given a set of positive numbers, partition the
set into two subsets with a minimum difference between their subset sums.
"""


def minimum_subset_sum(nums):
    if len(nums) == 0:
        return 0

    return min_sum(nums, 0, 0, 0)


def min_sum(nums, index, s1, s2):
    if index >= len(nums):
        return abs(s1 - s2)

    return min(
        min_sum(nums, index + 1, s1 + nums[index], s2),
        min_sum(nums, index + 1, s1, s2 + nums[index])
    )


# O(n * c) where n is len(nums) and c is sum(nums)
def minimum_subset_sun_memo(nums):
    if len(nums) == 0:
        return 0

    s = sum(nums)
    dp = [[-1 for _ in range(s + 1)] for _ in range(len(nums))]
    return min_sum_memo(dp, nums, 0, 0, 0)


def min_sum_memo(dp, nums, i, s1, s2):
    if i >= len(nums):
        return abs(s1 - s2)

    if dp[i][s1] == -1:
        diff1 = min_sum_memo(dp, nums, i + 1, s1 + nums[i], s2)
        diff2 = min_sum_memo(dp, nums, i + 1, s1, s2 + nums[i])

        dp[i][s1] = min(diff1, diff2)
    return dp[i][s1]


def minimum_sum_tabul(nums):
    if len(nums) == 0:
        return 0

    s = sum(nums) // 2
    n = len(nums)

    dp = [[False for _ in range(s + 1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = True

    # the case where we have 1 item
    for j in range(s + 1):
        dp[0][j] = j == nums[0]

    for i in range(1, n):
        for j in range(1, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = True
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]

    j = s
    while j >= 0:
        if dp[n - 1][j]:
            return abs((sum(nums) - j) - j)
        j -= 1


def main():
    print('brute')
    print(minimum_subset_sum([1, 2, 3, 9]))
    print(minimum_subset_sum([1, 2, 7, 1, 5]))
    print(minimum_subset_sum([1, 3, 100, 4]))

    print('\nmemo')
    print(minimum_subset_sun_memo([1, 2, 3, 9]))
    print(minimum_subset_sun_memo([1, 2, 7, 1, 5]))
    print(minimum_subset_sun_memo([1, 3, 100, 4]))

    print('\ntabul')
    print(minimum_sum_tabul([1, 2, 3, 9]))
    print(minimum_sum_tabul([1, 2, 7, 1, 5]))
    print(minimum_sum_tabul([1, 3, 100, 4]))


main()
