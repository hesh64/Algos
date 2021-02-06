"""
Implement a function, find_product(lst), which modifies a list so that each index has a product of all the
numbers present in the list except the number stored at that index.
"""


# Time O(n + n)
# Space O(n)
def find_product(lst):
    prod = 1
    zero_index = -1
    zeros = 0
    for i, el in enumerate(lst):
        if el == 0:
            zeros += 1
            zero_index = i
        if el != 0:
            prod *= el

    if zeros > 1:
        return [0] * len(lst)

    if zeros:
        zer = [0] * len(lst)
        zer[zero_index] = prod
        return zer

    return [(prod // el) for el in lst]


def main():
    lst = [1, 2, 3, 4]
    result = find_product(lst)
    print(result)
    lst = [0, 2, 3, 4]
    result = find_product(lst)
    print(result)


main()
