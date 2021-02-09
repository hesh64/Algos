"""
Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

"""


def find_subset_sum(array, s):
    if sum(array) < s:
        return False

    return find_subset_sum_rec(array, s, 0)


def find_subset_sum_memo(array, s):
    if sum(array) < s:
        return False

    memo = [[-1 for _ in range(s)] for _ in range(len(array))]

    return find_subset_sum_rec(array, s, 0)


def find_subset_sum_rec(array, s, index):
    if index >= len(array):
        return False

    if s == 0:
        return True

    right = False
    if array[index] <= s:
        right = find_subset_sum_rec(array, s - array[index], index + 1)

    return right or find_subset_sum_rec(array, s, index + 1)


def find_subset_sum_rec_memo(array, s, memo, index=0):
    if index >= len(array):
        return False

    if s == 0:
        return True

    if memo[index][s] != -1:
        return memo[index][s]

    right = False
    if array[index] <= s:
        right = find_subset_sum_rec(array, s - array[index], index + 1)

    memo[index][s] = right or find_subset_sum_rec(array, s, index + 1)
    return memo[index][s]


def main():
    su = [1, 2, 3, 7]
    s = 6
    result = find_subset_sum(su, s)
    print(result)

    su = [1, 2, 3, 7]
    s = 6
    result = find_subset_sum_memo(su, s)
    print(result)

    # s = [1, 1, 3, 4, 7]
    # result = find_subset_sum(s)
    # print(result)


main()
