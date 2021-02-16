"""In this problem, you have to implement the find_sum(lst,k) function which will
take a number k as input and return two numbers that add up to k.
"""


# Time O(n)
# Space O(n)
def find_sum(lst, k):
    seen = {}

    for e in lst:
        if e in seen:
            return [seen[e], e]
        else:
            seen[k - e] = e

    return [-1, -1]


def find_sum_sorted(lst, k):
    lst.sort()

    start, end = 0, len(lst) - 1

    while start < end:
        value = lst[start] + lst[end]

        if value < k:
            start += 1
        elif value > k:
            end -= 1
        elif value == k:
            return [lst[start], lst[end]]

    return [-1, -1]


def main():
    lst, k, = [1, 21, 3, 14, 5, 60, 7, 6], 81
    [left, right] = find_sum(lst, k)
    print(left, right)

    lst, k, = [1, 21, 3, 14, 5, 60, 7, 6], 81
    [left, right] = find_sum_sorted(lst, k)
    print(left, right)


main()
