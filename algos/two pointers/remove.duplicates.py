"""
Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space; after removing the duplicates in-place return
 the length of the subarray that has no duplicate in it.

"""


# O(n)
def remove_duplicates(array):
    ptr1 = 1
    ptr2 = 2

    while ptr2 < len(array):
        if array[ptr1 - 1] != array[ptr2]:
            array[ptr1] = array[ptr2]
            ptr1 += 1
        ptr2 += 1

    return ptr1


"""
Problem 1: Given an unsorted array of numbers and a target ‘key’,
 remove all instances of ‘key’ in-place and return the new length of the array.
"""


# O(n)
def remove_target(array, k):
    ptr1, ptr2 = 0, 1

    while ptr2 < len(array):
        if array[ptr2] != k:
            array[ptr1] = array[ptr2]
            ptr1 += 1
        ptr2 += 1

    print(array)
    return ptr1


def main():
    result = remove_duplicates([2, 3, 3, 6, 9, 9])
    print(result)

    result = remove_target([3, 2, 3, 6, 3, 10, 9, 3], k=3)
    print(result)

    result = remove_target([2, 11, 2, 2, 1], k=2)
    print(result)


main()
