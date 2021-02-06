"""
Implement a function findMinimum(lst) which finds the smallest number in the given list.

"""


# O(n)
# O(1)
def find_minimum(lst):
    if not len(lst):
        return None
    
    mini = float('inf')
    for ele in lst:
        if mini > ele:
            mini = ele
    return mini


def main():
    lst = [1, 2, 3, 4]
    result = find_minimum(lst)
    print(result)
    lst = [0, 2, 3, 4]
    result = find_minimum(lst)
    print(result)


main()
