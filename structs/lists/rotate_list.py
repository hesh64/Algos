"""
Implement a function right_rotate(lst, k) which will rotate the given list by k. This means that the right-most
elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element
at a time.
"""

# todo come back to this


def right_rotate(lst, k):
    length = len(lst)

    for i in range(k):
        lst[i], lst[length - (k + i + 1)] = lst[length -(k + i + 1)], lst[i]

    return lst


def main():
    lst, k = [10, 20, 30, 40, 50], 3
    result = right_rotate(lst, k)
    print(result)


main()
