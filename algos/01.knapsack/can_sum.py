"""
Given a set of positive numbers, determine if there exists
a subset whose sum is equal to a given number ‘S’.
"""


def subset_sum(nums, s):
    if len(nums) == 0:
        return False

    if sub_sum_rec(nums, s, 0):
        return True

    return False


def sub_sum_rec(nums, s, i):
    if s == 0:
        return True

    if i >= len(nums):
        return False

    if nums[i] <= s:
        if sub_sum_rec(nums, s - nums[i], i + 1):
            return True

    return sub_sum_rec(nums, s, i + 1)


def main():
    result = subset_sum([1, 2, 3, 7], 6)
    print(result)

    result = subset_sum([1, 2, 7, 1, 5], 10)
    print(result)

    result = subset_sum([1, 3, 4, 8], 6)
    print(result)


main()
