"""
Given a sorted array,
create a new array containing squares of all the numbers of the input array in the sorted order.

"""


def square(array):
    ptr1, ptr2 = 0, len(array) - 1
    squared = []

    while ptr1 <= ptr2:
        if (array[ptr1] ** 2) < (array[ptr2] ** 2):
            squared.insert(0, array[ptr2] ** 2)
            ptr2 -= 1
        else:
            squared.insert(0, array[ptr1] ** 2)
            ptr1 += 1

    return squared


"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
"""


def triplets(array):
    found = []
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if i != j and j != k and k != i:
                    if sum([array[i], array[j], array[k]]) == 0 and sorted([array[i], array[j], array[k]]) not in found:
                        found.append([array[i], array[j], array[k]])
    return found


def main():
    result = square([-2, -1, 0, 2, 3])
    print(result)

    result = triplets([-3, 0, 1, 2, -1, 1, -2])
    print(result)


main()
