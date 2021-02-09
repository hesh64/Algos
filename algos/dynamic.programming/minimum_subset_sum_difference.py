"""
Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.
"""

# O(2 ^ n)
def can_partition_minimum(nums):
    return can_partition_recursive(nums, 0, 0, 0)


def can_partition_recursive(nums, index, sum1, sum2):
    if index == len(nums):
        return abs(sum1 - sum2)

    diff1 = can_partition_recursive(nums, index + 1, sum1 + nums[index], sum2)
    diff2 = can_partition_recursive(nums, index + 1, sum1, sum2 + nums[index])

    return min(diff1, diff2)


# what an elegant solution..
def can_partition_minimum_memo(nums):
    memo = [[-1 for _ in range(sum(nums) + 1)] for _ in range(len(nums))]
    return can_partition_recursive_memo(nums, 0, 0, 0, memo)


def can_partition_recursive_memo(nums, index, sum1, sum2, memo):
    if index == len(nums):
        return abs(sum1 - sum2)

    if memo[index][sum1] == -1:
        diff1 = can_partition_recursive(nums, index + 1, sum1 + nums[index], sum2)
        diff2 = can_partition_recursive(nums, index + 1, sum1, sum2 + nums[index])

        memo[index][sum1] = min(diff1, diff2)

    return memo[index][sum1]


def main():
    nums = [1, 2, 3, 9]
    result = can_partition_minimum(nums)
    print(result)


main()
