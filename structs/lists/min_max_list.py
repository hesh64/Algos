"""
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th
index will have the largest number, the 1st index will have the smallest, and the third index will have
second-largest, and so on. In other words, all the odd-numbered indices will have the largest numbers in the list
in descending order and the even-numbered indices will have the smallest numbers in ascending order.

"""


# O(n)
# O(n)
def min_max(lst):
    left, right = 0, len(lst) - 1
    new_list = []

    while left < right:
        new_list.append(lst[right])
        right -= 1
        new_list.append(lst[left])
        left += 1

    if left == right:
        new_list.append(lst[left])

    return new_list


# todo this is an o(1) space solution, but i am not sure how to implement it

def main():
    lst = [1, 2, 3, 4, 5]
    result = min_max(lst)
    print(result)


main()
