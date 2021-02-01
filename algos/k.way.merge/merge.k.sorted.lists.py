class LinkedNode:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

    def __repr__(self):
        return f'{self.val}->{self.next}'

    def __lt__(self, other):
        return self.val < other.val


"""
Merge K Sorted Lists (medium)

Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
"""

from heapq import *


# We are assuming that we are allowed to edit lists
# Worst case, just make a new lists list with 'cur' pointers
# and apply the same logic
# Time O(k + n*log(k)) => O(n*log(k))
# Space O(n) where n is the amount of all the elements in all the lists
def merge_k_sorted_lists(lists):
    min_heap = []
    new_list = []
    # O(k) we have k many lists
    for i in range(len(lists)):
        if lists[i] is not None:
            heappush(min_heap, (lists[i].val, i))
            lists[i] = lists[i].next

    # O(k) at the most we are appending only 1 elements from each list so at the most
    # we'll have k elements!
    while min_heap:
        value, idx = heappop(min_heap)
        new_list.append(value)

        # O(log(n))
        if lists[idx] is not None:
            heappush(min_heap, (lists[idx].val, idx))
            lists[idx] = lists[idx].next

    return new_list


def main():
    l1 = LinkedNode(2, LinkedNode(6, LinkedNode(8)))
    l2 = LinkedNode(3, LinkedNode(6, LinkedNode(7)))
    l3 = LinkedNode(1, LinkedNode(3, LinkedNode(4)))
    lists = [l1, l2, l3]
    result = merge_k_sorted_lists(lists)
    print(result)

    l1 = LinkedNode(5, LinkedNode(8, LinkedNode(9)))
    l2 = LinkedNode(1, LinkedNode(7))
    l3 = LinkedNode(1, LinkedNode(3, LinkedNode(4)))
    lists = [l1, l2, l3]
    result = merge_k_sorted_lists(lists)
    print(result)


main()
