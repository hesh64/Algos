"""
Given a set of positive numbers (non zero) and a target sum ‘S’.
Each number should be assigned either a ‘+’ or ‘-’ sign.
We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.

"""


def target_sum(nums, s):
    if len(nums) == 0:
        return 0

    return target_sum_rec(nums, s, 0, 0)


def target_sum_rec(nums, s, t, i):
    if s == t and i == len(nums):
        return 1

    elif i == len(nums):
        return 0

    return target_sum_rec(nums, s, t + nums[i], i + 1) \
           + target_sum_rec(nums, s, t - nums[i], i + 1)


def main():
    set, s = [1, 1, 2, 3], 1
    result = target_sum(set, s)
    print(result)

    set, s = [1, 2, 7, 1], 9
    result = target_sum(set, s)
    print(result)


main()
