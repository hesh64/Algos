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


def main():
    array, key = [4, 6, 10], 10
    result = order_agnostic_binary_search(array=[4, 6, 10], key=10)
    print(f'find {key} in {array}', result)

    array.reverse()
    result = order_agnostic_binary_search(array=[10, 6, 4], key=10)
    print(f'find {key} in {array}', result)


main()
