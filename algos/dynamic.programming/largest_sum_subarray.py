"""Given an array, find the contiguous subarray with the largest sum.
"""


# Kadanes algo
# O(n) time
# O(1) space
def largest_sum_subarray(array):
    global_max, cur_max = array[0], array[0]

    for i in range(1, len(array)):
        if cur_max < 0:
            cur_max = array[i]
        else:
            cur_max += array[i]

        global_max = max(global_max, cur_max)

    return global_max


def main():
    array = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
    result = largest_sum_subarray(array)
    print(result)


main()
