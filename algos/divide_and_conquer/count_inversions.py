import random
import time

random.seed(0)


def measure(fn):
    def _(*args, **kwargs):
        now = time.time()
        res = fn(*args, **kwargs)
        print('it took', time.time() - now)
        return res

    return _


@measure
def count_inversion_brute_force(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1

    return count


@measure
def outside(array):
    return sort_and_count_inv(array)


def sort_and_count_inv(array):
    if len(array) <= 1:
        return 0, array

    mid = len(array) // 2

    (c, left) = sort_and_count_inv(array[:mid])
    (d, right) = sort_and_count_inv(array[mid:])
    (b, split) = merge_and_count_inv(left, right)

    return c + d + b, split


def merge_and_count_inv(left, right):
    if len(left) == 0:
        return 0, right
    if len(right) == 0:
        return 0, left

    c = 0
    p = [None] * (len(left) + len(right))
    i, j = 0, 0

    for k in range(len(p)):
        if i < len(left) and j < len(right):
            if left[i] < right[j]:
                p[k] = left[i]
                i += 1
            else:
                p[k] = right[j]
                c += len(left) - i
                j += 1
        elif i < len(left):
            p[k] = left[i]
            i += 1

        elif j < len(right):
            p[k] = right[j]
            j += 1

    return c, p


def main():
    arr = [1, 3, 5, 2, 4, 6]
    print('num of inversion is:', count_inversion_brute_force(arr))
    print('num of inversion is:', sort_and_count_inv(arr))

    arr = [6 - i for i in range(6)]
    print('num of inversion is:', count_inversion_brute_force(arr))
    print('num of inversion is:', sort_and_count_inv(arr))

    arr = [1, 3, 5, 2, 4, 6, 9, 7, 10, 8]
    print('num of inversion is:', count_inversion_brute_force(arr))
    print('num of inversion is:', sort_and_count_inv(arr))

    arr = [6 - i for i in range(10)]
    print('num of inversion is:', count_inversion_brute_force(arr))
    print('num of inversion is:', sort_and_count_inv(arr))

    arr = [12, 1, 11, 3, 5, 2, 4, 6, 9, 7, 10, 8]
    print('num of inversion is:', count_inversion_brute_force(arr))
    print('num of inversion is:', sort_and_count_inv(arr))

    arr = [6 - i for i in range(12)]
    print('num of inversion is:', count_inversion_brute_force(arr))
    print('num of inversion is:', sort_and_count_inv(arr))

    s = {random.randint(-60000, 60000) for _ in range(10000)}
    arr = list(s)
    print(len(arr))
    print('num of inversion is:', count_inversion_brute_force(arr))
    print('num of inversion is:', outside(arr)[0])


main()
