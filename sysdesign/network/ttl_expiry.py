from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


# O(n) time and space what a world
def get_devices(root, server, ttl):
    server_id = server.val
    g = {}

    def dfs(root):
        nonlocal g
        if root:
            if root.val not in g:
                g[root.val] = set()
            for child in root.children:
                if child not in g:
                    g[child.val] = set()
                g[child.val].add(root.val)
                g[root.val].add(child.val)
                dfs(child)

    dfs(root)
    visited = set()
    q = deque()
    q.append(server_id)
    visited.add(server_id)
    while q and ttl > 0:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            for child in g[node]:
                if child not in visited:
                    visited.add(node)
                    q.append(child)
        ttl -= 1
    return list(q)


def main():
    # Driver code
    root = TreeNode(1)
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(3))
    root.children.append(TreeNode(4))
    root.children[0].children.append(TreeNode(5))
    root.children[0].children[0].children.append(TreeNode(10))
    root.children[0].children.append(TreeNode(6))
    root.children[0].children[1].children.append(TreeNode(11))
    root.children[0].children[1].children.append(TreeNode(12))
    root.children[0].children[1].children.append(TreeNode(13))
    root.children[2].children.append(TreeNode(7))
    root.children[2].children.append(TreeNode(8))
    root.children[2].children.append(TreeNode(9))

    server = root.children[0].children[1]
    ttl = 2
    print("The TTL value will expire on node IDs:", get_devices(root, server, ttl))


main()
