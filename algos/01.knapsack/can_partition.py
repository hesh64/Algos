"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of
elements in both the subsets is equal.
"""


def can_partition(nums):
    s = sum(nums)

    if s % 2 != 0:
        return False

    if can_part_rec(nums, s // 2, 0):
        return True

    return False


def can_part_rec(nums, target, index):
    if target == 0:
        return True

    if index >= len(nums):
        return False

    if nums[index] <= target:
        if can_part_rec(nums, target - nums[index], index + 1):
            return True

    return can_part_rec(nums, target, index + 1)


def can_partition_memo(nums):
    s = sum(nums)
    if s % 2 != 0:
        return False

    s = s // 2
    dp = [[False for _ in range(s + 1)] for _ in range(len(nums))]
    return can_part_rec_memo(dp, nums, s, 0)


def can_part_rec_memo(dp, nums, target, index):
    if target == 0:
        return True

    if index >= len(nums):
        return False

    if not dp[index][target]:
        if can_part_rec_memo(dp, nums, target - nums[index], index + 1):
            dp[index][target] = True
            return True
        dp[index][target] = can_part_rec_memo(dp, nums, target, index + 1)

    return dp[index][target]


def can_partition_tabul(nums):
    s = sum(nums)
    if s % 2 != 0:
        return False

    if len(nums) == 0:
        return True

    s = s // 2
    n = len(nums)
    dp = [[False for _ in range(s + 1)] for _ in range(n)]

    # we can have an empty set when any number of subsets
    # so we basically initialize the first column to True (col 0)
    for i in range(n):
        dp[i][0] = True

    # this is for the case when we have a single digit in the
    # set
    for j in range(s + 1):
        dp[0][j] = j == nums[0]

    for i in range(1, n):
        for j in range(1, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = True
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]

    return dp[n - 1][s]


"""
Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.
"""


def subset_sum(nums, s):
    n = len(nums)

    if n == 0:
        return False

    return subset_sum_rec(nums, s, 0)


def subset_sum_rec(nums, s, index):
    if s == 0:
        return True

    if index >= len(nums):
        return False

    if nums[index] <= s:
        if subset_sum_rec(nums, s - nums[index], index + 1):
            return True

    return subset_sum_rec(nums, s, index + 1)


def subset_sum_memo(nums, s):
    n = len(nums)

    if n == 0:
        return False

    dp = [[-1 for _ in range(s + 1)] for _ in range(n)]

    return subset_sum_rec_memo(dp, nums, s, 0)


def subset_sum_rec_memo(dp, nums, s, index):
    if s == 0:
        return True

    if index >= len(nums):
        return False

    if dp[index][s] == -1:
        if nums[index] <= s:
            if subset_sum_rec_memo(dp, nums, s - nums[index], index + 1):
                dp[index][s] = True
                return True

        dp[index][s] = subset_sum_rec_memo(dp, nums, s, index + 1)
    return dp[index][s]


def subset_sum_tabul(nums, s):
    n = len(nums)

    if n == 0:
        return False

    dp = [[False for _ in range(s + 1)] for _ in range(n)]

    # initialize empty subset
    for j in range(n):
        dp[j][0] = True

    # if we have 1 item in the set then:
    for j in range(1, s + 1):
        dp[0][j] = j == nums[0]

    for i in range(1, n):
        for j in range(1, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = True
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]

    return dp[n - 1][s]


def main():
    print('can_parition')
    print('brute')
    result = can_partition([1, 1, 3, 4, 7])
    print(result)
    result = can_partition([2, 3, 4, 6])
    print(result)
    result = can_partition([1, 2, 3, 4])
    print(result)

    print('\nmemo')
    result = can_partition_memo([1, 1, 3, 4, 7])
    print(result)
    result = can_partition_memo([2, 3, 4, 6])
    print(result)
    result = can_partition_memo([1, 2, 3, 4])
    print(result)

    print('\ntabul')
    result = can_partition_tabul([1, 1, 3, 4, 7])
    print(result)
    result = can_partition_tabul([2, 3, 4, 6])
    print(result)
    result = can_partition_tabul([1, 2, 3, 4])
    print(result)

    print('\nsubset_sum')
    print('brute')
    result = subset_sum([1, 2, 3, 7], 6)
    print(result)
    result = subset_sum([1, 2, 7, 1, 5], 10)
    print(result)
    result = subset_sum([1, 3, 4, 8], 6)
    print(result)

    print('\nmemo')
    result = subset_sum_memo([1, 2, 3, 7], 6)
    print(result)
    result = subset_sum_memo([1, 2, 7, 1, 5], 10)
    print(result)
    result = subset_sum_memo([1, 3, 4, 8], 6)
    print(result)

    print('\ntabul')
    result = subset_sum_tabul([1, 2, 3, 7], 6)
    print(result)
    result = subset_sum_tabul([1, 2, 7, 1, 5], 10)
    print(result)
    result = subset_sum_tabul([1, 3, 4, 8], 6)
    print(result)


main()
