# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class BTree:
#     def __init__(self, rootval):
#         self.root = Node(rootval)
#
#     def _insert(self, head, val):
#         if head.val < val:
#             if head.right:
#                 self._insert(head.right, val)
#             else:
#                 head.right = Node(val)
#
#         elif head.val > val:
#             if head.left:
#                 self._insert(head.left, val)
#             else:
#                 head.left = Node(val)
#
#     def insert(self, val):
#         self._insert(self.root, val)
#         return True
#
#     def _pre(self, node, fn):
#         if node is None:
#             return
#
#         self._pre(node.right, fn)
#         fn(node)
#         self._pre(node.left, fn)
#
#     def pre(self, fn):
#         self._pre(self.root, fn)
#
#     def bf(self, fn):
#         q = [self.root]
#         idx = 0
#         while idx < len(q):
#             item = q[idx]
#             if item.left:
#                 q.append(item.left)
#
#             if item.right:
#                 q.append(item.right)
#             fn(item)
#             idx += 1
#
#     def bfs(self, val):
#         found = []
#         self.bf(lambda x: found.append(x) if x.val == val else None)
#         return found[0]
#
#     def df_iterative(self, fn):
#         stack = [self.root]
#         while len(stack):
#             node = stack.pop()
#             fn(node)
#
#             # left child will be on top so we
#             # push the right first
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#
#     def _df_recursive(self, root, fn):
#         if root is None:
#             return
#
#         # preorder
#         fn(root)
#         self._df_recursive(root.left, fn)
#         self._df_recursive(root.right, fn)
#         # post order
#         # self._df_recursive(root.left, fn)
#         # self._df_recursive(root.right, fn)
#         # fn(root)
#         # in order
#         # self._df_recursive(root.left, fn)
#         # fn(root)
#         # self._df_recursive(root.right, fn)
#
#     def df_recursive(self, fn):
#         self._df_recursive(self.root, fn)
#
#
# bt = BTree(10)
# bt.insert(3)
# bt.insert(13)
# bt.insert(2)
# bt.insert(4)
# bt.insert(12)
# bt.insert(1)
#
# bt.pre(lambda node: print(node.val))
# print('bf')
# bt.bf(lambda node: print(node.val))
# print('---')
# bt.df_iterative(lambda node: print(node.val))
# print('another one')
# bt.df_recursive(lambda node: print(node.val))
# print('found', bt.bfs(4).val)
#
# print('***\n\n')


class LinkedNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = LinkedNode(4, left=LinkedNode(2, left=LinkedNode(1), right=LinkedNode(3)), right=LinkedNode(5))


# first, last = None, None
#
# def in_order(root):
#     global last, first
#
#     if root:
#         in_order(root.left)
#
#         if last:
#             last.right = root
#             root.left = last
#
#         last = root
#         if first is None:
#             first = last
#
#         in_order(root.right)
#
# in_order(root)
#
# first.left, last.right = last, first
#
# i = 0
# curf = first
# curb = first
# while i < 20:
#     # print(curf.value)
#     print(curf.value, curb.value)
#     curf = curf.right
#     curb = curb.left
#     i += 1


# root = LinkedNode(4, left=LinkedNode(2,
#           left=LinkedNode(1), right=LinkedNode(3)), right=LinkedNode(5))


def get_ancestor(x, y, root):
    def get_lists(node):
        if node:

            if not node.right or not node.left:
                return [[node.value]]

            left = get_lists(node.left)
            right = get_lists(node.right)

            for l in left:
                l.append(node.value)

            for r in right:
                r.append(node.value)

            return left + right

        return []

    lists = get_lists(root)
    one, two = [l for l in lists if l[0] == x or l[0] == y]

    l = min([len(one), len(two)])
    j = 0
    while j < l:
        if one[j] == two[j]:
            return one[j]
        j += 1


print(get_ancestor(1, 3, root))
