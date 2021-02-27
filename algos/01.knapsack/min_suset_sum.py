"""
Given a set of positive numbers, partition the set
into two subsets with a minimum difference between their subset sums.
"""
import math


def min_subset_sum(nums):
    if len(nums) == 0:
        return None

    return min_rec(nums, 0, 0, 0)


def min_rec(nums, index, sum1, sum2):
    if index == len(nums):
        return abs(sum1 - sum2)

    diff1 = min_rec(nums, index + 1, sum1 + nums[index], sum2)
    diff2 = min_rec(nums, index + 1, sum1, sum2 + nums[index])

    return min(diff1, diff2)


def min_subset_sum_m(nums):
    if len(nums) == 0:
        return None

    dp = [[]]
    return min_rec_memo(nums, 0, 0, 0)


def min_rec_memo(nums, index, sum1, sum2):
    if index == len(nums):
        return abs(sum1 - sum2)

    diff1 = min_rec(nums, index + 1, sum1 + nums[index], sum2)
    diff2 = min_rec(nums, index + 1, sum1, sum2 + nums[index])

    return min(diff1, diff2)


def main():
    print("Can partition: " + str(min_subset_sum([1, 2, 3, 9])))
    print("Can partition: " + str(min_subset_sum([1, 2, 7, 1, 5])))
    print("Can partition: " + str(min_subset_sum([1, 3, 100, 4])))


main()
