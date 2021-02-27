"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of
elements in both the subsets is equal.
"""


def can_partition(nums):
    # if len(nums) % 2 != 0:
    #     return False

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


def main():
    result = can_partition([1, 1, 3, 4, 7])
    print(result)
    result = can_partition([2, 3, 4, 6])
    print(result)
    result = can_partition([1, 2, 3, 4])
    print(result)

main()