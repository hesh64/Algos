def merge_sort(array, start, end):
    if end - start > 1:
        mid = start + (end - start) // 2
        # print('beofre', array[start: mid], array[mid: end])

        merge_sort(array, start, mid), merge_sort(array, mid, end)
        # print('after', array[start: mid], array[mid: end])

        merge(array, start, mid, end)
        # print('mrege', array[start: end])

    return array


def merge(arr, start, mid, end):
    k, i, j = start, start, mid
    # print(array[start: mid], array[mid: end])
    while k < end:
        if i < mid and j < end:
            if arr[i] < arr[j]:
                i += 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        else:
            break


if __name__ == '__main__':
    arr = [9, 81, 71, 16, 100, 991, 1, 0, 20, 60, 43]
    print(merge_sort(arr, 0, len(arr)))
    # merge([71, 16, 100], 0, 1, 3)
    # arr = [71, 16, 100]
    # start, mid, end = 0, 1, 3
    # i, j, k = start, mid, start
    # while i < mid or j < end:
    #     if i < mid and j < end:
    #         if arr[i] < arr[j]:
    #             i += 1
    #         else:
    #             arr[i], arr[j] = arr[j], arr[i]
    #             j += 1
    #     else:
    #         break
    print(arr)
