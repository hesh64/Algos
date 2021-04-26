"""
Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than
a given ‘key’.

Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first
letter. This also means that the smallest letter in the given array is greater than the last letter of the array and
is also the first letter of the array.

Write a function to return the next letter of the given ‘key’
"""


def smallest_letter(array, key):
    start, end = 0, len(array) - 1

    if array[-1] < key or array[0] > key:
        return array[0]

    while start <= end:
        mid = start + (end - start) // 2

        if array[mid] >= key:
            end = mid - 1
        else:
            start = mid + 1

    # 7 % 3 is = subtracts as many 3s out of 7 that's the modulo so 7 - 3= 4, 4 -3 = 1. 7 % 3 = 1 surprise
    return array[start % len(array)]


"""
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range 
of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].
"""


def number_range(array, key):
    start, end = 0, len(array) - 1

    k = -1
    while start <= end:
        mid = start + (end - start) // 2

        if array[mid] > key:
            end = mid - 1
        elif array[mid] < key:
            start = mid + 1
        else:
            k = mid
            break

    if k == -1:
        return [-1, -1]

    l, r = k, k

    while l - 1 >= 0 and r + 1 < len(array):
        if array[l - 1] == array[k] or array[r + 1] == array[k]:
            if array[l - 1] == array[k]:
                l -= 1
            else:
                r += 1
        else:
            break

    return [l, r]


def main():
    result = smallest_letter(['a', 'c', 'f', 'h'], key='f')
    print('smallest_letter', result)

    result = smallest_letter(['a', 'c', 'f', 'h'], key='b')
    print('smallest_letter', result)

    result = smallest_letter(['a', 'c', 'f', 'h'], key='m')
    print('smallest_letter', result)

    result = smallest_letter(['a', 'c', 'f', 'h'], key='h')
    print('smallest_letter', result)

    result = number_range([4, 6, 6, 6, 9], key=6)
    print('smallest_letter', result)

    result = number_range([1, 3, 8, 10, 15], key=10)
    print('smallest_letter', result)

    result = number_range([1, 3, 8, 10, 15], key=12)
    print('smallest_letter', result)


main()
