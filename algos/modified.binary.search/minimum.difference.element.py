def min_diff_element(array, key):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] > key:
            end = mid - 1

        elif array[mid] < key:
            start = mid + 1

        else:
            return array[mid]

    if start >= len(array):
        return array[end]

    if end < 0:
        return array[start]

    if key - array[end] < key - array[start]:
        return array[end]

    return array[start]


"""
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and 
then monotonically decreasing. Monotonically increasing or decreasing means that for any
index i in the array arr[i] != arr[i+1].
"""


def bitonic_array_max(array):
    start, end = 0, len(array) - 1
    # diff 1 start must be less than not less than or equal to
    while start < end:
        mid = start + (end - start) // 2

        if array[mid] > array[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return array[start]


"""
Search Bitonic Array (medium) #
Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically
increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the 
array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.
"""


# first find the middle
def search_bitonic_array(array, key):
    start, end = 0, len(array) - 1

    while start < end:
        mid = start + (end - start) // 2

        if array[mid] > array[mid + 1]:
            end = mid
        else:
            start = mid + 1

    max_index = start

    # now search for the value in between the monotonic ranges
    found = binary_search_both(array, key, 0, max_index + 1)
    if found != -1:
        return found
    return binary_search_both(array, key, max_index, len(array) - 1)


def binary_search_both(array, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2

        if array[mid] == key:
            return mid

        # this goes both ways.
        if array[start] <= array[end]:
            if array[mid] > key:
                start = mid + 1
            else:
                end = mid - 1
        else:
            # array start > array end
            if array[mid] > key:
                end = mid + 1
            else:
                start = mid - 1

    return -1


def main():
    array, key = [4, 6, 8, 10], 7
    result = min_diff_element(array, key)
    print(result)

    array, key = [4, 6, 10], 4
    result = min_diff_element(array, key)
    print(result)

    array, key = [1, 3, 8, 10, 15], 12
    result = min_diff_element(array, key)
    print(result)

    array, key = [4, 6, 10], 17
    result = min_diff_element(array, key)
    print(result)

    array, key = [4, 6, 10], 3
    result = min_diff_element(array, key)
    print(result)

    array = [1, 3, 8, 12, 4, 2]
    result = bitonic_array_max(array)
    print(result)

    array = [3, 8, 3, 1]
    result = bitonic_array_max(array)
    print(result)

    array, key = [1, 3, 8, 4, 3], 4
    result = search_bitonic_array(array, key)
    print(result)


main()
