import random
from collections import deque

random.seed(10)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.right_child is None and node.left_child is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right_child is None:
        lines, n, p, x = _display_aux(node.left_child)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left_child is None:
        lines, n, p, x = _display_aux(node.right_child)
        s = str(node.val)
        u = len(s)
        #        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.left_child)
    right, m, q, y = _display_aux(node.right_child)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
                 '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
                  (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


class Node:
    def __init__(self, val):
        self.val = val
        self.left_child, self.right_child, self.parent = None, None, None


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert_recursive(self, val):
        def _rec(root, _val):
            if not root:
                return

            if val < root.val and root.left_child:
                return _rec(root.left_child, val)
            if val < root.val:
                root.left_child = Node(val)

            if root.val < val and root.right_child:
                return _rec(root.right_child, val)
            if root.val < val:
                root.right_child = Node(val)

        return _rec(self.root, val)

    def insert_iterative(self, val):
        cur = self.root
        parent = None

        while cur:
            parent = cur

            if cur.val > val:
                cur = cur.left_child
            else:
                cur = cur.right_child

        if val < parent.val:
            parent.left_child = Node(val)
        else:
            parent.right_child = Node(val)

    def search_recursive(self, val):
        def _rec(root, _val):
            if not root:
                return -1

            if root.val == _val:
                return root

            if _val < root.val and root.left_child:
                return _rec(root.left_child, _val)

            if _val < root.val:
                return -1

            if root.val < _val and root.right_child:
                return _rec(root.left_child, _val)

            if root.val < _val:
                return -1

            return -1

    def search_iterative(self, val):
        cur = self.root

        while cur and cur.val != val:
            if val < cur.val:
                cur = cur.left_child
            elif cur.val < val:
                cur = cur.right_child

        if cur and cur.val == val:
            return cur

        return -1

    def delete(self, val):
        def _delete(root, _val):
            if val < root.val:
                if root.left_child:
                    root.left_child = _delete(root.left_child, _val)
                else:
                    return None

            elif val > root.val:
                if root.right_child:
                    root.right_child = _delete(root.right_child, _val)
                else:
                    return None

            else:  # this root is the value
                print(160)
                # this root is a leaf
                if root.left_child is None and root.right_child is None:
                    print(164)
                    return None
                # you only have a right child
                elif root.left_child is None:
                    print(167)
                    return root.right_child
                # you only have a left child
                elif root.right_child is None:
                    return root.left_child
                else:
                    print(170)
                    # we wanna find the min of the right subtree
                    # that's our choice we can also decide to find
                    # the max of the left subtree
                    current = root.right_child
                    while current.left_child is not None:
                        current = current.left_child

                    root.val = current.val
                    root.right_child = _delete(root.right_child, current.val)

            return root

        _delete(self.root, val)

    def pre_order(self):
        def pre(root):
            if root:
                print(root.val)
                pre(root.left_child)
                pre(root.right_child)

        return pre(self.root)

    def post_order(self):
        def post(root):
            if root:
                post(root.left_child)
                post(root.right_child)
                print(root.val)

        return post(self.root)

    def in_order(self):
        def in_or(root):
            if root:
                in_or(root.left_child)
                print(root.val)
                in_or(root.right_child)

        return in_or(self.root)

    def kth_largest(self, k):
        """Given the root to a Binary Search Tree and a number "k" write a
        function to find the kth maximum value in the tree. A solution is placed in
        the "solution" section for your help, but we would suggest you to solve it on your own first."""
        if k <= 0:
            return None

        counter = 0
        cur_max = None

        def _kth_largest(root, _k):
            nonlocal cur_max, counter
            if not root:
                return None

            node = _kth_largest(root.right_child, _k)
            if _k != counter and root.val != cur_max:
                counter += 1
                cur_max = root.val
                # you need to set this because we
                # return node
                node = root

            if _k == counter:
                return node

            return _kth_largest(root.left_child, _k)

        node = _kth_largest(self.root, k)
        if node:
            return node.val

        return None

    # time avg O(log(n)), O(n) at the worst
    # space avg O(log(n)), O(n) at worst
    def get_ancestors(self, k):
        ancestors = []
        cur = self.root

        while cur:
            if cur.val > k:
                ancestors.insert(cur.val)
                cur = cur.left_child
            elif cur.val < k:
                ancestors.insert(0, cur.val)
                cur = cur.right_child
            else:
                return ancestors

        return -1

    # O(n)
    # O(n) at the worst, avg O(log(n))
    def find_height(self):
        def _h(root):
            if not root:
                return -1

            return max(_h(root.left_child), _h(root.right_child)) + 1

        return _h(self.root)

    def find_k_from_root(self, k):
        def _from(root, k):
            q = deque()
            q.append(root)
            depth = 0
            nodes_at_depth = []

            while q:
                depth += 1
                size = len(q)
                for _ in range(size):
                    node = q.popleft()
                    if k - 1 == depth:
                        nodes_at_depth.append(node.val)

                if len(nodes_at_depth) > 0:
                    return nodes_at_depth

            return nodes_at_depth

        return _from(self.root, k)

    # at the worst it'll be O(n), avg O(2^k) where 2^k < n
    def find_k_from_root_rec(self, k):
        nodes = []

        def _from(root, _k, depth=0):
            nonlocal nodes
            if not root:
                return

            if _k == depth:
                nodes.append(root.val)

            elif _k > depth:
                _from(root.left_child, _k, depth + 1)
                _from(root.right_child, _k, depth + 1)

        _from(self.root, k)
        return nodes


def main():
    BST = BinarySearchTree(50)
    for _ in range(15):
        ele = random.randint(0, 100)
        # print("Inserting " + str(ele) + ":")
        BST.insert_recursive(ele)
        # # We have hidden the code for this function but it is available for use!
        # display(BST.root)
        # print('\n')

    display(BST.root)
    # BST.delete(50)
    # display(BST.root)
    # BST.pre_order()
    # print('\n')
    # BST.post_order()
    # print('\n')
    # BST.in_order()
    print(BST.kth_largest(4))


main()
