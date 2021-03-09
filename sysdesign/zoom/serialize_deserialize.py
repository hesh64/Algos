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


class Translator:
    # O(n)
    def serialize(self, root):
        res = []

        def pre_order(root):
            if root:
                res.append(root.val + ',')
                pre_order(root.left)
                pre_order(root.right)

        pre_order(root)
        return ''.join(res)

    # O(n)
    def deserialize(self, data):
        lst = data.split(',')
        lst.pop()
        root = None
        for n in lst:
            if not root:
                root = BST()
                root.insert(n)
            else:
                root.insert(n)

        return root.root


def main():
    names = ["Jeanette", "Elia", "Albert", "Latasha", "Elvira", "Kandice", "Maggie"]
    root = BST()
    for n in names:
        root.insert(n)

    tran = Translator()
    string = tran.serialize(root.root)
    print(string)

    def pre_order(root):
        if root:
            print(root.val)
            pre_order(root.left)
            pre_order(root.right)

    root_1 = tran.deserialize(string)
    pre_order(root_1)


main()
