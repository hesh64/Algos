"""
Implement a function right_rotate(lst, k) which will rotate the given list by k. This means that the right-most
elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element
at a time.
"""


# time O(n)
# space O(n)
def right_rotate(lst, k):
    rotated = []
    for ele in lst[len(lst) + 1 - k:]:
        rotated.append(ele)

    for ele in lst[: len(lst) + 1 - k]:
        rotated.append(ele)

    return rotated


def main():
    lst, k = [10, 20, 30, 40, 50], 3
    result = right_rotate(lst, k)
    print(result)


main()
