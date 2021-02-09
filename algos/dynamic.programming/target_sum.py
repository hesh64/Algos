"""
You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign.
We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’
"""


def target_sum(nums, target):
    sums = []
    target_sum_recursive(nums, target, 0, [], sums)
    return sums


def target_sum_recursive(nums, target, index, cur_set, sums):
    if index == len(nums) and target != 0:
        return

    if index == len(nums) and target == 0:
        sums.append(cur_set)
        return

    positive = cur_set.copy()
    positive.append(nums[index])
    target_sum_recursive(nums, target + nums[index], index + 1, positive, sums)

    negative = cur_set.copy()
    negative.append(-nums[index])
    target_sum_recursive(nums, target + -nums[index], index + 1, negative, sums)


def main():
    nums, s = [1, 1, 2, 3], 1
    result = target_sum(nums, s)
    print(result)


main()
