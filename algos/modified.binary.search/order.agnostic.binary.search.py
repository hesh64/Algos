"""
Order-agnostic Binary Search (easy)
Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
Though we know that  array is sorted, we don’t know if it’s sorted in ascending or
descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array,
otherwise return -1.
"""


def order_agnostic_binary_search(array, key):
    start, end = 0, len(array) - 1
    asce = array[start] < array[end]

    while start <= end:
        mid = (end + start) // 2

        if array[mid] == key:
            return mid

        if asce:
            if array[mid] < key:
                start = mid + 1

            else:
                end = mid - 1
        else:
            if array[mid] < key:
                end = mid - 1

            else:
                start = mid + 1

    return -1


"""
Ceiling of a Number

Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the 
‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.
"""


def ceiling_of_a_number(array, key):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] >= key:
            if mid > 0 and array[mid - 1] < key:
                return mid
            elif mid == 0:
                return mid

        if array[mid] > key:
            end = mid - 1

        else:
            start = mid + 1

    return -1


def search_ceiling(array, key):
    if key > array[-1]:
        return -1

    start, end = 0, len(array) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if key < array[mid]:
            end = mid - 1
        elif key > array[mid]:
            start = mid + 1
        else:
            return mid

    return start


"""

Similar Problems #
Problem 1 #
Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’. The floor of the ‘key’ 
will be the biggest element in the given array smaller than or equal to the ‘key’
"""


def search_floor(array, key):
    start, end = 0, len(array) - 1

    if array[-1] < key:
        return -1
    # check this condition out.
    # you won't ever break out of the loop unless you get to the point
    # where end < start with exception for the value being in the array.
    # keep that in mind, don't stop drawing out the calculations until
    # you hit 
    while start <= end:
        mid = start + (end - start) // 2

        if array[mid] > key:
            end = mid - 1

        elif array[mid] < key:
            start = mid + 1

        else:
            return mid

    return end


def main():
    array, key = [4, 6, 10], 10
    result = order_agnostic_binary_search(array=[4, 6, 10], key=10)
    print(f'find {key} in {array}', result)

    array.reverse()
    result = order_agnostic_binary_search(array=[10, 6, 4], key=10)
    print(f'find {key} in {array}', result)

    array, key = [4, 6, 10], 6
    result = ceiling_of_a_number(array, key)
    print(result)

    array, key = [3, 4, 5, 6, 7, 8, 10], 6
    result = ceiling_of_a_number(array, key)
    print(result)

    array, key = [1, 3, 8, 10, 15], 12
    result = ceiling_of_a_number(array, key)
    print(result)

    array, key = [4, 6, 10], 17
    result = ceiling_of_a_number(array, key)
    print(result)

    array, key = [4, 6, 10], -1
    result = ceiling_of_a_number(array, key)
    print(result)


main()
