def number_range(array, key):
    between = [-1, -1]

    between[0] = binary_search_modified(array, key, False)

    if between[0] != -1:
        between[1] = binary_search_modified(array, key)

    return between


def binary_search_modified(array, key, find_max=True):
    start, end = 0, len(array) - 1
    index = -1

    while start <= end:
        mid = start + (end - start) // 2

        if array[mid] > key:
            end = mid - 1

        elif array[mid] < key:
            start = mid + 1

        else:
            # you know that mid is equal to key
            index = mid
            '''if we made it here then array[mid] == key but now we wanna find where
            the range starts and ends'''
            if find_max:
                # we wanna find the max so move up start by one, remember you wanna fool the while
                # loop into thinking that we didn't find the answer yet, and that start should
                # move up.
                start = mid + 1
            else:
                # literally the opposite
                end = mid - 1

    # this is wild!
    return index


def main():
    array, key = [4, 6, 6, 6, 9], 6
    result = number_range(array, key)
    print(result)

    array, key = [1, 3, 8, 10, 15], 10
    result = number_range(array, key)
    print(result)

    array, key = [1, 3, 8, 10, 15], 12
    result = number_range(array, key)
    print(result)


main()
