class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def max_clock_skew(root):
    max_diff = 0

    def dfs(root, max_val, min_val):
        nonlocal max_diff
        if root:
            min_val = min(min_val, root.val)
            max_val = max(max_val, root.val)
            for child in root.children:
                dfs(child, max_val, min_val)

            if max_val != -float('inf') and min_val != float('inf'):
                max_diff = max(max_diff, max_val - min_val)

    dfs(root, -float('inf'), float('inf'))
    return max_diff


def main():
    # Driver code
    root = TreeNode(8)
    root.children.append(TreeNode(3))
    root.children.append(TreeNode(10))
    root.children.append(TreeNode(12))
    root.children[0].children.append(TreeNode(6))
    root.children[0].children[0].children.append(TreeNode(1))
    root.children[0].children.append(TreeNode(5))
    root.children[0].children[1].children.append(TreeNode(2))
    root.children[0].children[1].children.append(TreeNode(3))
    root.children[0].children[1].children.append(TreeNode(4))
    root.children[2].children.append(TreeNode(8))
    root.children[2].children.append(TreeNode(7))
    root.children[2].children.append(TreeNode(9))

    print("The maximum clock skew we'll encounter is:", max_clock_skew(root), "seconds")


main()
