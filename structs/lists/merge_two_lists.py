"""
Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.
 Name it merge_lists(lst1, lst2).

"""


def merge_lists(lst1, lst2):
    i, j = 0, 0
    new_list = []
    while i < len(lst1) or j < len(lst2):
        if i < len(lst1) and j < len(lst2) and lst1[i] < lst2[j]:
            new_list.append(lst1[i])
            i += 1
        elif i < len(lst1) and j < len(lst2) and lst1[i] > lst2[j]:
            new_list.append(lst2[j])
            j += 1
        elif i < len(lst1):
            new_list.append(lst1[i])
            i += 1
        else:
            new_list.append(lst2[j])
            j += 1

    return new_list


def merge_lists_in_place(lst1, lst2):
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst2[j] < lst1[i]:
            lst1.insert(i, lst2[j])
            j += 1
        else:
            i += 1

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
