"""
Implement a function find_second_maximum(lst) which returns the second largest element in the list.

"""


# O(n)
# O(1)
def find_second_max(lst):
    larger, smaller = max(lst[0], lst[1]), min(lst[0], lst[1])

    for i in range(2, len(lst)):
        ele = lst[i]
        if ele > larger:
            smaller = larger
            larger = ele

        elif ele > smaller:
            smaller = ele

    return smaller


def main():
    lst = [1, 2, 3, 4]
    result = find_second_max(lst)
    print(result)

    lst = [0, 2, 3, 4]
    result = find_second_max(lst)
    print(result)

    lst = [3, 4]
    result = find_second_max(lst)
    print(result)

    lst = [3, 4, 0, -1]
    result = find_second_max(lst)
    print(result)


main()
