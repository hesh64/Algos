class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
Tree Diameter (medium) #
Given a binary tree, find the length of its diameter. The diameter of a tree is the 
number of nodes on the longest path between any two leaf nodes. The diameter of a tree may
or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.
"""


def tree_diameter(root):
    max_diam = 0

    def _tree_diameter(root):
        nonlocal max_diam
        if root:
            left, right = 0, 0
            if root.left:
                left = _tree_diameter(root.left)
            if root.right:
                right = _tree_diameter(root.right)

            max_diam = max(left + right + 1, max_diam)
            return max(left, right) + 1

        return 0

    _tree_diameter(root)
    return max_diam


"""
Path with Maximum Sum (hard) #
Find the path with the maximum sum in a given binary tree. 
Write a function that returns the maximum sum.

A path can be defined as a sequence of nodes between any two nodes and doesn’t
necessarily pass through the root. The path must contain at least one node.


"""


def path_with_max_sum(root):
    max_sum = 0

    def _path_with_max_sum(root):
        nonlocal max_sum
        if root:
            left, right = 0, 0
            if root.left:
                left = _path_with_max_sum(root.left)
            if root.right:
                right = _path_with_max_sum(root.right)

            max_sum = max(left + right + root.value, max_sum)
            return max(left, right) + root.value

        return 0

    _path_with_max_sum(root)
    return max_sum


def main():
    head = Node(1)
    head.left = Node(2)
    head.left.right = Node(4)
    head.right = Node(3)
    head.right.left = Node(5)
    head.right.right = Node(6)

    print('tree diameter is:', tree_diameter(head))
    print('tree diameter is:', path_with_max_sum(head))

    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.right.left = Node(5)
    head.right.left.left = Node(7)
    head.right.left.right = Node(8)
    head.right.left.right.right = Node(10)
    head.right.right = Node(6)
    head.right.right.right = Node(9)
    head.right.right.right.right = Node(11)

    print('tree diameter is:', tree_diameter(head))
    print('tree diameter is:', path_with_max_sum(head))


main()
