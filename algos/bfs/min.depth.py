from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value}'


def binary_tree_level_order_traversal_min(node):
    nodes = []

    if not node:
        return nodes

    queue = deque()
    queue.append(node)
    depth = 0
    while queue:
        depth += 1
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            curr_node = queue.popleft()
            if not curr_node.left and not curr_node.right:
                return depth

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            current_level.append(curr_node)
        nodes.append(current_level)

    return nodes


def binary_tree_level_order_traversal_level_order_traversal(node, val):
    nodes = []

    if not node:
        return nodes

    queue = deque()
    queue.append(node)
    return_the_next = False

    while queue:

        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            curr_node = queue.popleft()
            if return_the_next:
                return curr_node.value

            if curr_node.value == val:
                return_the_next = True

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            current_level.append(curr_node)
        nodes.append(current_level)

    return None


"""
Problem Statement #
Given a binary tree, connect each node with its level order successor. 
The last node of each level should point to a null node.


"""


def binary_tree_level_order_traversal_level_order_traversal_connected(node):
    nodes = []

    if not node:
        return nodes

    queue = deque()
    queue.append(node)
    while queue:
        level_size = len(queue)
        current_level = []
        last_node = None
        for _ in range(level_size):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            if last_node:
                last_node.right = curr_node

            last_node = curr_node

            current_level.append(curr_node)
        if last_node:
            last_node.right = None
        nodes.append(current_level)

    return nodes


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    min_level = binary_tree_level_order_traversal_min(root)
    print('minimum level is:', min_level)

    min_level = binary_tree_level_order_traversal_level_order_traversal(root, 1)
    print('successor:', min_level)

    min_level = binary_tree_level_order_traversal_level_order_traversal(root, 3)
    print('successor:', min_level)

    min_level = binary_tree_level_order_traversal_level_order_traversal(root, 6)
    print('minimum level is:', min_level)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.right.left = Node(6)
    root2.right.right = Node(7)

    head_connected = binary_tree_level_order_traversal_level_order_traversal_connected(root)
    print(head_connected)
    for i in range(len(head_connected)):
        head = head_connected[i][0]
        while head:
            print(head.value)
            head = head.right
        print('end of linked list...')


main()
