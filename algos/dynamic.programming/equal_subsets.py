"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of
elements in both subsets is equal.

if we find just 1 subset that's equal to half the sum of the set,
then is guarenteed we have a second set with that same sum
"""


# O(2^n)
# O(n)
def find_partition(nums):
    s = sum(nums)
    print(s)
    if s % 2 != 0:
        return False

    return find_partition_brute(nums, s // 2)


def find_partition_brute(nums, half_sum, index=0):
    if half_sum == 0:
        return True

    if index >= len(nums) or len(nums) == 0:
        return False

    if nums[index] <= half_sum:
        if find_partition_brute(nums, half_sum - nums[index], index + 1):
            return True

    return find_partition_brute(nums, half_sum, index + 1)


# O(2^n)
# O(n)
def find_partition_memo(nums):
    s = sum(nums)
    print(s)
    if s % 2 != 0:
        return False

    memo = [[-1 for i in range((s // 2) + 1)] for _ in range(len(nums))]

    return find_partition_rec_memo(nums, s // 2, memo)


# O(n * s) - s is the total sum of all numbers
# O(n* s)
def find_partition_rec_memo(nums, half_sum, memo, index=0):
    if half_sum == 0:
        return True

    if index >= len(nums) or len(nums) == 0:
        return False

    if memo[index][half_sum] != -1:
        return memo[index][half_sum]

    if nums[index] <= half_sum:
        memo[index][half_sum] = find_partition_brute(nums, half_sum - nums[index], index + 1)
        if memo[index][half_sum] is True:
            return True

    memo[index][half_sum] = find_partition_brute(nums, half_sum, index + 1)
    return memo[index][half_sum]


def main():
    s = [1, 1, 3, 4, 7]
    result = find_partition(s)
    print(result)

    s = [1, 1, 3, 4, 7]
    result = find_partition_memo(s)
    print(result)


main()
