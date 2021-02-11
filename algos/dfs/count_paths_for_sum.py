class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each 
path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from 
parent to child (top to bottom).
"""


# O(n^2) at the worst case O(n) for iterating the tree, and another O(n) for iterating the subarray of node
# O(n) because of the recursive calls
def count_paths_for_sum(root, s):
    return count_path_rec(root, s, [])


def count_path_rec(root, s, path):
    # if not root return 0
    if not root:
        return 0

    # what is the path sum beginning this node?
    # how many paths meet the sum beginning this node?
    path_sum, path_count = 0, 0

    # append this node to the global path list
    path.append(root)

    # for every node in the path from end to start sum the nodes up
    # and if at some point they add up to s this works be going from
    # a lower level to the root.
    for i in range(len(path) - 1, -1, -1):
        path_sum += path[i].value

        if path_sum == s:
            path_count += 1

    # now let's add also the count from paths that include the left child
    path_count += count_path_rec(root.left, s, path)
    # now let's add also the count from paths that include the right child
    path_count += count_path_rec(root.right, s, path)

    # say we are 2 levels in and we are finished looking
    # pop this leave off the path so that the next leaf can
    # hop on. This is our way of backtracking
    del path[-1]

    # return the total path count
    return path_count


"""
Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.

A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root. 
The path must contain at least one node."""


def find_max_path_sum(root):
    max_global_sum = -float('inf')

    def max_sum_rec(node):
        nonlocal max_global_sum

        # base case
        if node is None:
            return 0

        # ignore the paths with ngative sums
        left_sum = max(max_sum_rec(node.left), 0)
        right_sum = max(max_sum_rec(node.right), 0)

        # local maximum sum
        max_local_sum = node.value + left_sum + right_sum
        # set the global sum
        max_global_sum = max(max_global_sum, max_local_sum)

        return max(left_sum, right_sum) + node.value

    max_sum_rec(root)
    return max_global_sum


def main():
    root = Node(1)
    root.left = Node(7)
    root.left.left = Node(6)
    root.left.right = Node(5)
    root.right = Node(9)
    root.right.left = Node(2)
    root.right.right = Node(3)

    result = count_paths_for_sum(root, 12)
    print(result)

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    result = find_max_path_sum(root)
    print(result)

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    result = find_max_path_sum(root)
    print(result)


main()
