# when in rome
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
Problem Statement #
Given a binary tree and a number ‘S’, find if the tree has a path from
root-to-leaf such that the sum of all the node values of that path equals ‘S’.
"""


def has_path(root, val):
    if root:
        if root.value == val and not root.left and not root.right:
            return True

        return has_path(root.left, val - root.value) or has_path(root.right, val - root.value)

    return False


"""
Given a binary tree and a number ‘S’, find all paths from root-to-leaf
such that the sum of all the node values of each path equals ‘S’.
"""


def all_paths_for_a_sum(root, val):
    if root:
        if root.value == val and not root.left and not root.right:
            result = deque()
            result.appendleft(root.value)
            return [result]

        left, right = all_paths_for_a_sum(root.left, val - root.value), \
                      all_paths_for_a_sum(root.right, val - root.value)

        if not left and not right:
            return []

        left = left if left else []
        right = right if right else []

        left.extend(right)

        for l in left:
            l.appendleft(root.value)

        return left

    return []


"""
Problem 1: Given a binary tree, return all root-to-leaf paths.
"""


def root_to_leaf(root):
    if root:
        if not root.left and not root.right:
            result = deque()
            result.appendleft(root.value)
            return [result]

        left, right = root_to_leaf(root.left), root_to_leaf(root.right)

        if not left and not right:
            return []

        left = left if left else []
        right = right if right else []

        left.extend(right)

        for l in left:
            l.appendleft(root.value)

        return left

    return []


"""
Given a binary tree, find the root-to-leaf path with the
 maximum sumGiven a binary tree, find the root-to-leaf path with the maximum sum
"""


def max_sum(root):
    def _max_sum(_root, s=0):
        if _root:
            new_sum = _root.value + s
            return max(_max_sum(_root.left, new_sum), _max_sum(_root.right, new_sum))

        return s

    return _max_sum(root)


def main():
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)

    result = has_path(head, 10)
    print(result)

    head = Node(12)
    head.left = Node(7)
    head.right = Node(1)
    head.left.right = Node(4)
    head.right.left = Node(10)
    head.right.right = Node(5)

    result = has_path(head, 23)
    print('has path for 23', result)
    result = has_path(head, 16)
    print('has path for 16', result)

    result = all_paths_for_a_sum(head, 23)
    print('all paths to 23', result)
    result = all_paths_for_a_sum(head, 16)
    print('all paths to 16', result)

    print('root to leaf paths', root_to_leaf(head))

    print('max path sum is: ', max_sum(head))


main()
