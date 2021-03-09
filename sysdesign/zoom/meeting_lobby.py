from collections import deque


class BinaryNode:
    def __init__(self, val):
        self.right, self.left = None, None
        self.val = val


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = BinaryNode(val)
            return

        cur = self.root
        while cur:
            if cur.val < val and cur.right:
                cur = cur.right
            elif cur.val < val:
                cur.right = BinaryNode(val)
                return

            if cur.val > val and cur.left:
                cur = cur.left
            elif cur.val > val:
                cur.left = BinaryNode(val)
                return


class DisplayLobby:
    def __init__(self, bst):
        self.bst = bst.root
        self.stack = deque()
        self.push_all(bst.root)

    def push_all(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def has_next(self):
        return len(self.stack) != 0

    def next_name(self):
        if self.has_next():
            node = self.stack.pop()
            if node.right:
                self.push_all(node.right)
            return node.val
        return None

    def next_page(self):
        if self.has_next():
            return [self.next_name() for i in range(10)]
        return []


import random


def main():
    names = ["Jeanette", "Latasha", "Elvira", "Caryl", "Antoinette", "Cassie", "Charity", "Lyn", "Elia", "Anya",
             "Albert", "Cherlyn", "Lala", "Kandice", "Iliana"]

    bst = BST()
    for w in names:
        bst.insert(w)

    dn = DisplayLobby(bst)
    print(dn.next_page())
    print(dn.next_page())
    print(dn.next_page())


main()
