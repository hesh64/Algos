"""
Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.
 Name it merge_lists(lst1, lst2).

"""


def merge_lists(lst1, lst2):
    i, j = 0, 0
    new_list = []
    while i < len(lst1) or j < len(lst2):
        if lst1[i] < lst2[j]:
            new_list.append(lst1[i])
            i += 1
        else:
            new_list.append(lst2[j])
            j += 1

    return new_list


# lst1 len = n
# lst2 len = m
# time is O(m(n+m)) or O(n^2)
# space is O(m)
#  there is a clear tradeoff with the previous solution between time and space
def merge_lists_in_place(lst1, lst2):
    i, j = 0, 0

    # at most will run m times
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            i += 1
        else:
            # will cost n
            lst1.insert(i, lst2[j])
            j += 1
            i += 1

    # because of the cost associated with inserts
    # this can be as expensive as O(nm)

    # in case this is valid, we can assume that the previous loop cost us
    # n^2 and so this one costs
    if j < len(lst2):
        lst1.append(lst2[j:])

    return lst1


def main():
    list1 = [1, 3, 4, 5]
    list2 = [2, 6, 7, 8]

    result = merge_lists(list1, list2)
    print(result)

    list1, list2 = [4, 5, 6], [-2, -1, 0, 7]
    result = merge_lists(list1, list2)
    print(result)

    list1 = [1, 3, 4, 5]
    list2 = [2, 6, 7, 8]

    result = merge_lists_in_place(list1, list2)
    print(result)

    list1, list2 = [4, 5, 6], [-2, -1, 0, 7]
    result = merge_lists_in_place(list1, list2)
    print(result)


main()
