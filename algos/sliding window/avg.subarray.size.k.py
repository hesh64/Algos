# Time complexity of O((n - k) * k)
# n = # of array elements
# k = size of the window

def average_subarray_of_size_k(k, array):
    sub = []
    i = 0

    while i + k <= len(array):
        s = 0
        for j in range(i, k + i):
            s += array[j]

        sub.append(s / k)
        i += 1

    return sub


# Time complexity of O(n)
# n = # of array elements
# k = size of the window
def average_subarray_of_size_k2(k, array):
    sub = []
    _sum = sum(array[:k])
    sub.append(_sum / k)
    first = 0

    for i in range(1, len(array) - k + 1):
        _sum -= array[first]
        _sum += array[k - 1 + i]
        sub.append(_sum / k)
        first += 1

    return sub


# slight variation where we compare the sums
# and store the max one
# Time Complexity O(n)
# Space O(1)
def find_max_sum_subarray_k(k, array):
    max_sum = -1
    last_index = 0
    sliding_sum = 0
    for i in range(len(array)):
        sliding_sum += array[i]
        if i > k - 1:
            sliding_sum -= array[last_index]
            last_index += 1

        max_sum = max(max_sum, sliding_sum)

    return max_sum


# O((n-1) * n) -> O(n^2)
def find_length_smallest_subarray_w_sum(s, array):
    min_l = len(array) + 1

    # n - 1
    for k in range(1, len(array)):
        last_index = 0
        sliding_sum = 0

        # n
        for i in range(len(array)):
            sliding_sum += array[i]
            if i >= k:
                sliding_sum -= array[last_index]
                last_index += 1

            if sliding_sum >= s:
                if min_l > k:
                    min_l = k

    return min_l


# can we do better?
# O(n + n)
# Space O(1)
def find_length_smallest_subarray_w_sum2(s, array):
    sliding_sum = 0
    min_length = len(array) + 1
    start = 0

    for end in range(len(array)):
        while sliding_sum >= s:
            min_length = min(min_length, end - start + 1)
            sliding_sum -= array[start]
            start += 1

    if min_length == len(array) + 1:
        return 0

    return min_length


def main():
    Array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    K = 5

    subs = average_subarray_of_size_k(K, Array)
    print(subs, '\n')

    subs = average_subarray_of_size_k2(K, Array)
    print(subs, '\n')

    max_sum = find_max_sum_subarray_k(3, [2, 1, 5, 1, 3, 2])
    print('max sum:', max_sum, '\n')

    min_sum_len = find_length_smallest_subarray_w_sum(7, [2, 1, 5, 2, 3, 2])
    print('min length array for sum', min_sum_len, '\n')

    min_sum_len = find_length_smallest_subarray_w_sum(7, [2, 1, 5, 2, 8])
    print('min length array for sum', min_sum_len, '\n')


main()
