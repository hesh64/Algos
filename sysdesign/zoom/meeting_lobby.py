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
    # O(1) amortized
    # O(n) space
    def __init__(self, bst):
        self.bst = bst.root
        self.stack = deque()
        self.push_all(bst.root)

    # O(1) amortized time
    # in the worst case it'll be an O(n) for the first one
    # then an O(1) for any of the following ones
    # O(n) space
    def push_all(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    # O(1) space and time
    def has_next(self):
        return len(self.stack) != 0

    # O(1) Time amortized -- worst case would be when we push the root,
    # pop it then the rest of the tree would be in the right pointer
    # O(n) space
    def next_name(self):
        if self.has_next():
            node = self.stack.pop()
            if node.right:
                self.push_all(node.right)
            return node.val
        return None

    # O(1) amortized time, O(n) space
    def next_page(self):
        if self.has_next():
            return [self.next_name() for i in range(10)]
        return []


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
