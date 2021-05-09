from collections import namedtuple, deque


def bfs(n):
    que = deque()
    que.append(n)

    while que:
        size = len(que)
        row = []
        for i in range(size):
            n = que.popleft()
            row.append(n.data)

            if n.left:
                que.append(n.left)

            if n.right:
                que.append(n.right)

        print(row)


class BinaryTreeNode:
    def __init__(self, data):
        self.left, self.right = None, None
        self.data = data


def is_balanced_binary_tree(root):
    if not root:
        return True

    HeightWithBalance = namedtuple('HeightWithBalance', ('height', 'balanced'))

    def is_balanced(root):
        if root is None:
            return HeightWithBalance(-1, True)

        left, right = is_balanced(root.left), is_balanced(root.right)
        if left.balanced is False or right.balanced is False:
            return left if left.balanced is False else right

        check_balance = abs(left.height - right.height)
        return HeightWithBalance(1 + max(left.height, right.height), check_balance <= 1)

    return is_balanced(root).balanced


def is_balanced_brute_force(root):
    def get_max_depth(root):
        if root is None:
            return -1

        return 1 + max(get_max_depth(root.left), get_max_depth(root.right))

    def pre_order(root):
        if root is None:
            return True

        left, right = get_max_depth(root.left), get_max_depth(root.right)

        if abs(left - right) > 1:
            return False

        return True and is_balanced_brute_force(root.left) and is_balanced_brute_force(root.right)

    return pre_order(root)


# lowest common ancestor
def lca(root, n1, n2):
    n1path, n2path = None, None

    def find(root, stack):
        nonlocal n1path, n2path

        if root is None:
            return

        if root == n1:
            n1path = stack[:]
        if root == n2:
            n2path = stack[:]

        stack.append(root)
        find(root.left, stack)
        find(root.right, stack)
        stack.pop()

    find(root, [])
    i = 0
    while i < len(n1path) and i < len(n2path) and n1path[i] == n2path[i]:
        i += 1
    return n1path[i - 1]


def iter_in_order(root):
    stack, result = [], []
    stack.append((root, False))

    while stack:
        node, finished = stack.pop()
        if node and finished:
            result.append(node.data)
        elif node and not finished:
            stack.extend([
                (node.right, False),
                (node, True),
                (node.left, False),
            ])

    return result


def kth_node_in_inorder(root, k):
    stack, result = [], None

    stack.append((root, False))
    while stack:
        node, finished = stack.pop()
        if node and finished:
            result = node
            k -= 1
            if k == 0:
                return result

        elif node and finished is False:
            stack.extend([
                (node.right, False),
                (node, True),
                (node.left, False)
            ])

    return result


tree = BinaryTreeNode('A')
tree.left = BinaryTreeNode('B')
tree.right = BinaryTreeNode('K')
tree.right.right = BinaryTreeNode('O')
tree.right.left = BinaryTreeNode('L')
tree.right.left.left = BinaryTreeNode('M')
tree.right.left.right = BinaryTreeNode('N')
tree.left.left = BinaryTreeNode('C')
tree.left.right = BinaryTreeNode('H')
tree.left.right.left = BinaryTreeNode('I')
tree.left.right.right = BinaryTreeNode('J')
tree.left.left.left = BinaryTreeNode('D')
tree.left.left.right = BinaryTreeNode('G')
tree.left.left.left.left = BinaryTreeNode('E')
tree.left.left.left.right = BinaryTreeNode('F')

bfs(tree)

print('lca is:', lca(tree, tree.left.left.left.left, tree.left.right.left).data)

print(is_balanced_binary_tree(tree))
print(is_balanced_brute_force(tree))
print('iter_in_order', iter_in_order(tree))
print('return_kth_node_in_inorder', kth_node_in_inorder(tree, 3).data)

tree = BinaryTreeNode('A')
tree.left = BinaryTreeNode('B')
tree.right = BinaryTreeNode('C')
tree.left.left = BinaryTreeNode('E')
tree.left.right = BinaryTreeNode('F')
tree.left.left.left = BinaryTreeNode('G')

bfs(tree)
print(is_balanced_binary_tree(tree))
print(is_balanced_brute_force(tree))


def in_order_iter(root):
    last, cur = None, root
    while cur.left:
        last, cur = cur, cur.left

    while cur:
        if last and last is cur.right:
            while last is cur.right:
                last, cur = cur, cur.parent
                if cur is None:
                    return
        else:
            if cur.left and cur.left != last:
                while cur.left:
                    last, cur = cur, cur.left

            else:
                last, cur = cur, cur.right or cur.parent


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = self.right = None

    def __repr__(self):
        return f'{self.data}'


root = Node('A')
root.left = Node('B', root)
root.left.left = Node('C', root.left)
root.left.right = Node('D', root.left)
root.right = Node('E', root)
root.right.right = Node('F', root.right)
root.right.right.left = Node('G', root.right.right)

in_order_iter(root)


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left, self.right = left, right


inorder = ['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G']
preorder = ['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I']


# preorder head left right
# inorder left head right
def make_tree(preorder, inorder):
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    def make_tree_helper(preorder_start, preorder_end, inorder_start, inorder_end):
        print(preorder_start, preorder_end, inorder_start, inorder_end)
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        number_of_nodes_in_left_subtree = inorder_idx - inorder_start
        return Node(
            preorder[preorder_start],
            make_tree_helper(
                preorder_start + 1, preorder_start + 1 + number_of_nodes_in_left_subtree, inorder_start, inorder_idx),
            make_tree_helper(
                preorder_start + 1 + number_of_nodes_in_left_subtree, preorder_end, inorder_idx + 1, inorder_end
            )
        )

    return make_tree_helper(0, len(preorder), 0, len(inorder))


tree = make_tree(preorder, inorder)
bfs(tree)

preorder = ['H', 'B', 'F', None, None, 'E', 'A', None, None, None, 'C', None, 'D', None, 'G', 'I', None, None, None]


def make_tree_from_preorder_with_marks(preorder):
    def helper(preorder):
        if len(preorder) == 0:
            return None

        head = preorder.pop(0)
        if head is None:
            return

        return Node(head, helper(preorder), helper(preorder))

    return helper(preorder)


print('---')
tree = make_tree_from_preorder_with_marks(preorder)
bfs(tree)
