class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
Sum of Path Numbers (medium)
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent 
a number. Find the total sum of all the numbers represented by all paths.
"""


def sum_of_path_numbers(root, base_sum=0):
    if root:
        path_sum = 10 * base_sum + root.value

        if not root.left and not root.right:
            return path_sum

        return sum_of_path_numbers(root.left, path_sum) + sum_of_path_numbers(root.right, path_sum)

    return 0


"""
Path With Given Sequence (medium)
Given a binary tree and a number sequence,
 find if the sequence is present as a root-to-leaf path in the given tree.
"""


def path_to_leaf_with_sequence(root, seq):
    if not root:
        return len(seq) == 0

    def helper(root, seq, index=0):
        if not root:
            return False

        if root.value != seq[index] or index >= len(seq):
            return False

        if len(seq) - 1 == index and not root.left and not root.right:
            return True

        return helper(root.left, seq, index + 1) or helper(root.right, seq, index + 1)

    return helper(root, seq)


"""
Count Paths for a Sum (medium)
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the
 node values of each path equals ‘S’. Please note that the paths can start or end at any node b
 ut all paths must follow direction from parent to child (top to bottom).
"""


# def count_paths_for_sum
#     come back to this!

def main():
    head = Node(1)
    head.left = Node(7)
    head.right = Node(9)
    head.right.left = Node(2)
    head.right.right = Node(9)

    print('sum of path numbers:', sum_of_path_numbers(head))

    print('is there a path to lead with sequence: [1,9,9]?', path_to_leaf_with_sequence(head, [1, 9, 9]))
    print('is there a path to lead with sequence: [1,9,2]?', path_to_leaf_with_sequence(head, [1, 9, 2]))
    print('is there a path to lead with sequence: [1,9,1]?', path_to_leaf_with_sequence(head, [1, 9, 1]))
    print('is there a path to lead with sequence: [1,9,2,1]?', path_to_leaf_with_sequence(head, [1, 9, 2, 1]))


main()
