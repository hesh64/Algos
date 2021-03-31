def selection_sort(arr):
    p = 0
    # O(n)
    while p < len(arr):
        min_index = p
        # O(n)
        for i in range(p + 1, len(arr)):
            if arr[min_index] > arr[i]:
                min_index = i

        arr[min_index], arr[p] = arr[p], arr[min_index]
        p += 1

    return arr


def main():
    arr = [3, 2, 1, 5, 4]
    selection_sort(arr)
    print(arr)


main()
