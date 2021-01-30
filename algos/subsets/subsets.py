"""
Subsets
Problem Statement #
Given a set with distinct elements, find all of its distinct subsets.
"""


# O(n * 2^n)
def subset(nums):
    subsets = [[]]

    for num in nums:
        size = len(subsets)

        for i in range(size):
            sub1 = subsets[i].copy()
            sub1.append(num)
            subsets.append(sub1)

    return subsets


# O(n * 2^n)
def subset_w_duplicates(nums):
    nums.sort()
    subsets = [[]]
    start, end = 0, 0

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            start = end + 1

        end = len(subsets) - 1
        for j in range(start, end + 1):
            sub = list(subsets[j])
            sub.append(nums[i])
            subsets.append(sub)

    return subsets


def main():
    result = subset([1, 3])
    print(result)

    result = subset([1, 3, 5])
    print(result)

    result = subset([1, 3, 3])
    print(result)

    print('with dupes')
    result = subset_w_duplicates([1, 3, 3])
    print(result)

    result = subset_w_duplicates([1, 5, 3, 3])
    print(result)

    result = subset_w_duplicates([1, 1, 2, 2])
    print(result)


main()
