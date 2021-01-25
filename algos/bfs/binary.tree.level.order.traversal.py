from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value}'


def binary_tree_level_order_traversal(node):
    nodes = []

    if not node:
        return nodes

    queue = deque()
    queue.append(node)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            current_level.append(curr_node)
        nodes.append(current_level)

    return nodes


def binary_tree_level_order_traversal_reversed(node):
    nodes = []

    if not node:
        return nodes

    queue = deque()
    queue.append(node)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            current_level.append(curr_node)
        nodes.insert(0, current_level)

    return nodes


def binary_tree_level_order_traversal_zigzag(node):
    nodes = []

    if not node:
        return nodes

    # heads i go left to right
    # tails i go right to left
    left_to_right = True
    queue = deque()
    queue.append(node)
    while queue:
        level_size = len(queue)
        current_level = deque()
        for _ in range(level_size):
            curr_node = queue.popleft()

            if left_to_right:
                current_level.append(curr_node)
            else:
                current_level.appendleft(curr_node)

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        nodes.append(list(current_level))
        # flip it
        left_to_right = not left_to_right

    return nodes


def binary_tree_level_order_traversal_average(node):
    nodes = []

    if not node:
        return nodes

    queue = deque()
    queue.append(node)
    while queue:
        level_size = len(queue)
        level_sum = 0
        for _ in range(level_size):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            level_sum += curr_node.value
        nodes.append(level_sum / level_size)

    return nodes


def binary_tree_level_order_traversal_max_per_level(node):
    nodes = []

    if not node:
        return nodes

    queue = deque()
    queue.append(node)
    while queue:
        level_size = len(queue)
        level_max = 0
        for _ in range(level_size):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            level_max = max(level_max, curr_node.value)
        nodes.append(level_max)

    return nodes


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    nodes = binary_tree_level_order_traversal(root)
    print(nodes)

    nodes = binary_tree_level_order_traversal_reversed(root)
    print(nodes)

    nodes = binary_tree_level_order_traversal_zigzag(root)
    print(nodes)

    nodes = binary_tree_level_order_traversal_average(root)
    print(nodes)

    nodes = binary_tree_level_order_traversal_max_per_level(root)
    print(nodes)


main()
