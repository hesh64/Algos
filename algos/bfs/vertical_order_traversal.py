from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def vertical_order_traversal(root):
    map = {}
    que = deque()
    que.append((root, 0))

    while que:
        size = len(que)
        for _ in range(size):
            ele, i = que.popleft()
            if i not in map:
                map[i] = []
            map[i].append(ele.val)
            if ele.left:
                que.append((ele.left, i - 1))
            if ele.right:
                que.append((ele.right, i + 1))

    min_val, max_val = min(map.keys()), max(map.keys())
    results = []
    for i in range(min_val, max_val + 1):
        results.append(map[i])
    return results


def main():
    root = TreeNode(5)
    root.right = TreeNode(9)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(17)
    root.left = TreeNode(20)
    root.left.right = TreeNode(7)
    root.left.left = TreeNode(2)

    print(vertical_order_traversal(root))


main()
