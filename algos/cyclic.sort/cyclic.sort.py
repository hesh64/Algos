"""
Problem Statement #
We are given an array containing ‘n’ objects. Each object, when created, was assigned
a unique number from 1 to ‘n’ based on their creation sequence. This means that the
object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence number in O(n) and
without any extra space. For simplicity, let’s assume we are passed an integer array containing only
the sequence numbers, though each number is actually an object.


"""


# O(n)

def cyclic_sort(nums):
    i = 0

    while i < len(nums):
        target = nums[i] - 1

        if nums[target] != nums[i]:
            nums[i], nums[target] = nums[target], nums[i]
        else:
            i += 1

    return nums


"""
Problem Statement #
We are given an array containing ‘n’ distinct numbers taken from the range
 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

"""


# O(n)

def missing2(nums):
    i = 0

    while i < len(nums):
        target = nums[i]

        if target < len(nums) and nums[target] != nums[i]:
            nums[i], nums[target] = nums[target], nums[i]
        else:
            i += 1

    for ii in range(nums):
        if nums[ii] != ii:
            return ii

    return len(nums)


def missing_number(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(0, len(nums) - 1):
        if nums[i] != i:
            return i

    return n


"""
Problem Statement #
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array 
can have duplicates, which means some numbers will be missing. Find all those missing numbers.
"""


def missing_numbers(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing = []
    for i in range(0, len(nums) - 1):
        if nums[i] != i + 1:
            missing.append(i + 1)

    return missing


"""
Problem Statement #
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
The array has only one duplicate but it can be repeated multiple times. Find that duplicate number
without using any extra space. You are, however, allowed to modify the input array.
"""


def duplicate(nums):
    i = 0
    dup = None
    while i < len(nums):
        target = nums[i] - 1
        if nums[i] == nums[target]:
            dup = nums[i]

        if nums[target] != nums[i]:
            nums[i], nums[target] = nums[target], nums[i]
        else:
            i += 1


def main():
    result = cyclic_sort([3, 1, 5, 4, 2])
    print(result)
    result = cyclic_sort([1, 5, 6, 4, 3, 2])
    print(result)

    # result = missing2([4, 0, 3, 1])
    # print(result)

    result = missing_number([4, 0, 3, 1])
    print(result)

    result = missing_numbers([2, 3, 1, 8, 2, 3, 5, 1])
    print(result)


main()
