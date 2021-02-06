"""
Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the
left and positive elements appear at the right of the list. Note that it is not necessary to maintain the sorted order
of the input list.
"""""


# O(n)
# O(1) -> no new space used
def rearrange(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        if lst[left] > 0 and lst[right] < 0:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        if lst[left] < 0:
            left += 1
        if lst[right] > 0:
            right -= 1

    return lst


def main():
    lst = [10, -1, 20, 4, 5, -9, -6]
    result = rearrange(lst)
    print(result)


main()
