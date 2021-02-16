# time O(n)
# space O(n)
def first_none_repeating_element(lst):
    seen = {}

    for ele in lst:
        if ele not in seen:
            seen[ele] = 0
        seen[ele] += 1

    for ele in lst:
        if seen[ele] == 1:
            return ele

    return -1


# we can sacrifice time for lesser space
# time O(n^2)
# space O(1)
# two for loops -- brute force

def main():
    lst = [9, 2, 3, 2, 6, 6]
    product = first_none_repeating_element(lst)
    print(product)


main()
