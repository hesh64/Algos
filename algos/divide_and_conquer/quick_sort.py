import random
import time

random.seed(0)


def choose_pivot(a, l, r):
    return a[0]


def quick_sort(array, left, right):
    if left >= right:
        return

    i = choose_pivot(array, left, right)
    array[left], array[i] = array[i], array[left]
    j = partition(array, left, right)
    quick_sort(array, left, j - 1)
    quick_sort(array, j + 1, right)


def partition(array, start, end):
    i = start + 1

    for j in range(start + 1, end):
        if array[j] < array[start]:
            array[j], array[i] = array[i], array[j]
            i += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1


def main():
    arr = [3, 8, 2, 5, 1, 4, 7, 6]
    quick_sort(arr, 0, len(arr))
    print(arr)

    s = {random.randint(0, 60000) for _ in range(10)}
    arr = list(s)
    print(len(arr))
    quick_sort(arr, 0, len(arr))
    print(arr)
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            print('not sorted')
            break


main()
