def minimum_hops(array):
    val = min_hops(array, 0, 0)
    if val == len(array) + 1:
        return -1

    return val


def min_hops(arr, i, count):
    print('i', i, count)
    if i > len(arr):
        print(122222)
        return len(arr) + 1
    if i == len(arr):
        return count

    allowed = arr[i]
    # print('allowed', allowed)
    c = len(arr)
    for j in range(i + 1, i + allowed):
        # print('allowed', allowed, 'j', j)
        c = min(c, min_hops(arr, i + j, count + 1))

    return c


def main():
    switch_array = [2, 3, 1, 1, 4]
    print("Minimum hops to final router are:", minimum_hops(switch_array))
    switch_array = [4, 1, 1, 3, 1, 1, 1]
    print("Minimum hops to final router are:", minimum_hops(switch_array))


main()
