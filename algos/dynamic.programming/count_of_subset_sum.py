"""
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
"""


def count_subset_sum(nums, target):
    memo = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]
    return count_subset_sum_rec(nums, target, 0, memo)


def count_subset_sum_rec(nums, target, index, memo):
    if target == 0:
        return 1

    if index >= len(nums):
        return 0

    if memo[index][target] != -1:
        return memo[index][target]

    right = 0
    if nums[index] <= target:
        right = count_subset_sum_rec(nums, target - nums[index], index + 1, memo)

    left = count_subset_sum_rec(nums, target, index + 1, memo)

    memo[index][target] = right + left
    return memo[index][target]


def main():
    nums, s = [1, 1, 2, 3], 4
    result = count_subset_sum(nums, s)
    print(result)


main()
