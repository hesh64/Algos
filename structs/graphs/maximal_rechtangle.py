"""
Given a rows x cols binary matrix filled with 0's and 1's, find
the largest rectangle containing only 1's and return its area.




Input: matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
 """


def can_partition(nums):
    if len(nums) == 0 or len(nums) % 2 != 0:
        return False

    return helper(nums, 0, sum(nums) // 2)


def helper(nums, i, target_sum):
    print(nums, i, target_sum)
    if target_sum == 0:
        return True

    if len(nums) == 0 or i >= len(nums):
        return False

    if nums[i] <= target_sum:
        if helper(nums, i + 1, target_sum - nums[i]):
            return True

    return helper(nums, i + 1, target_sum)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
