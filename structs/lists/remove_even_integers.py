"""
Implement a function that removes all the even elements from a given list. Name it remove_even(list).
"""

# Time O(n)
# Space O(n)
def remove_event(l):
    return [i for i in l if i % 2 != 0]


def main():
    li = [1, 2, 3, 4, 5, 6, 7]
    result = remove_event(li)
    print(result)


main()
