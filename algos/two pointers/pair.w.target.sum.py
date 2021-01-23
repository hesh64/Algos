"""
Problem Statement #
Given an array of sorted numbers and a target sum, find a pair
 in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair)
 such that they add up to the given target.


"""


# O(n)
def sum(array, target):
    ptr1, ptr2 = 0, len(array) - 1

    while ptr1 < ptr2:
        val = array[ptr1] + array[ptr2]
        if val == target:
            return [ptr1, ptr2]

        if val > target:
            ptr2 -= 1

        else:
            ptr1 += 1

    return [-1, -1]


# O(n)
def sum_hashtable(array, target):
    table = {}
    for i in range(len(array)):
        y = target - array[i]
        if y in table:
            return [i, table[y]]
        else:
            table[array[i]] = i


def main():
    result = sum([1, 2, 3, 4, 6], target=6)
    print(result)

    result = sum([2, 5, 9, 11], target=11)
    print(result)

    result = sum_hashtable([1, 2, 3, 4, 6], target=6)
    print(result)

    result = sum_hashtable([2, 5, 9, 11], target=11)
    print(result)


main()
