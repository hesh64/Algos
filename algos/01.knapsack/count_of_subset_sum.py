"""
Given a set of positive numbers, find the total number of subsets
whose sum is equal to a given number ‘S’.

"""


def total_subsets(set, s):
    if len(set) == 0:
        return 0

    return total_rec(set, s, 0)


def total_rec(set, s, i):
    if s == 0:
        return 1

    if i >= len(set):
        return 0

    total = 0
    if set[i] <= s:
        total = total_rec(set, s - set[i], i + 1)

    return total_rec(set, s, i + 1) + total


def main():
    set, s = [1,1,2,3], 4
    result = total_subsets(set, s)
    print(result)

    set, s = [1,2, 7, 1, 5], 9
    result = total_subsets(set, s)
    print(result)



main()