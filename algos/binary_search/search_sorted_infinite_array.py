arr, key = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 16
max_integer = 10 ^ 6


class ArrayReader:
    def __init__(self, arr):
        self.array = arr
        self.max_integer = 10 ^ 6

    def get_index(self, index):
        if index < len(self.array):
            return self.array[index]
        else:
            return self.max_integer


def count_rotations(arr):
    def bs(arr):
        if arr[-1] > arr[0]:
            return 0

        start, end = 0, len(arr) - 1
        last = -1

        while start < end:
            mid = start + (end - start) // 2

            if arr[mid] >= arr[start]:
                start = mid + 1
            else:
                last = mid
                end = mid - 1

        return last if last > -1 else 0

    return bs(arr)


def main():
    arr, key = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 16
    array_reader = ArrayReader(arr)

    def bs(reader, key):
        diff = 2
        start, end = 0, 2

        while reader.get_index(start) < key:
            mid = start + (end - start) // 2
            print('mid', mid)
            mid_val = reader.get_index(mid)
            print('mid_val', mid_val)
            if mid_val == max_integer or mid_val > key:
                end = mid - 1
            elif key > mid_val:
                start = mid + 1
                diff *= diff
                end += diff
            else:
                return mid

        return -1

    print(bs(array_reader, key))
    print('--')
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()
