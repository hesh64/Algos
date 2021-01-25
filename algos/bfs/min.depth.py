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


main()
