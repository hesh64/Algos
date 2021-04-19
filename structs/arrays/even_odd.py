def even_odd(arr):
    i, even, odd = 0, 0, len(arr) - 1

    while even < odd:
        if arr[i] != 0 and arr[i] % 2 == 0:
            arr[even], arr[i] = arr[i], arr[even]
            even += 1
            i += 1
        elif arr[i] != 0 and arr[i] % 2 != 0:
            arr[odd], arr[i] = arr[i], arr[odd]
            odd -= 1
        else:
            i += 1


def dutch_flag_partition(arr, pivot):
    i, lo, hi = 0, 0, len(arr) - 1
    while lo < hi:
        if arr[i] < pivot:
            arr[lo], arr[i] = arr[i], arr[lo]
            lo += 1
            i += 1
        elif arr[i] > pivot:
            arr[hi], arr[i] = arr[i], arr[hi]
            hi -= 1
        else:
            i += 1


def d_plus_one(arr):
    carry = 1
    for i in range(len(arr) - 1, -1, -1):
        if carry == 0:
            break
        arr[i] += carry
        carry = 0
        if arr[i] > 9:
            arr[i] = arr[i] % 10
            carry = 1
    if carry > 0:
        arr.insert(0, 1)


def main():
    arr = [3, 11, -2, 2, 1, -6, -9, 10, 2, 101, -42, 0]
    even_odd(arr)
    print(arr)
    arr = [2, 1, -6, -9, 3, 11, -2, 10, 2, 101, -42, 0]
    even_odd(arr)
    print(arr)
    arr = [2, 1, -6, 11, -2, 10, 2, 101, -42, 0, -9, 3, ]
    even_odd(arr)
    print(arr)

    print('---')
    arr = [3, 11, -2, 2, 1, -6, -9, 10, 2, 101, -42, 0]
    dutch_flag_partition(arr, 1)
    print(arr)
    arr = [2, 1, -6, -9, 3, 11, -2, 10, 2, 101, -42, 0]
    dutch_flag_partition(arr, -2)
    print(arr)
    arr = [2, 1, -6, 11, -2, 10, 2, 101, -42, 0, -9, 3, ]
    dutch_flag_partition(arr, 11)
    print(arr)

    print('----')
    arr = [1, 2, 9]
    d_plus_one(arr)
    print(arr)

    arr = [9, 2, 9]
    d_plus_one(arr)
    print(arr)

    arr = [9, 9, 9]
    d_plus_one(arr)
    print(arr)


main()
