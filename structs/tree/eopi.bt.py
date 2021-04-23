class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


def iterative_inorder(root):
    prev = None
    while root:
        if prev is root.parent:
            if root.left:
                next = root.left

            else:
                print(root.data)
                next = root.right or root.parent
        elif prev is root.left:
            print(root.data)
            next = root.right or root.parent

        else:
            next = root.parent

        prev, root = root, next


def attach_parent(root):
    if root is None:
        return

    if root.left:
        root.left.parent = root
    if root.right:
        root.right.parent = root

    attach_parent(root.left)
    attach_parent(root.right)


def in_order(root, l=0):
    if root:
        in_order(root.left, l + 5)
        print(' ' * l + str(root.data))
        in_order(root.right, l + 5)


def main():
    root = Node(4, left=Node(5, left=Node(3), right=Node(6)), right=Node(12, left=Node(10), right=Node(11)))
    attach_parent(root)

    in_order(root)
    print('\n')
    iterative_inorder(root)


main()
