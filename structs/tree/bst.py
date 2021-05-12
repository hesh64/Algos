from collections import deque


class BSTNode:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def get_minmax(root):
    min_ptr = root
    while min_ptr.left:
        min_ptr = min_ptr.left

    max_ptr = root
    while max_ptr.right:
        max_ptr = max_ptr.right

    return min_ptr, max_ptr


def is_bst(root):
    def is_bst_helper(root, start, end):
        if not root:
            return True

        if start <= root.data <= end:
            return is_bst_helper(root.left, start, root.data) \
                   and is_bst_helper(root.right, root.data, end)

        return False

    return is_bst_helper(root, float('-inf'), float('inf'))


def is_bst_bfs(root):
    que = deque()
    que.append((root, float('-inf'), float('inf')))

    while que:
        size = len(que)
        for _ in range(size):
            n, lo, hi = que.popleft()
            if lo <= n.data <= hi:
                n.right and que.append((n.right, n.data, hi))
                n.left and que.append((n.left, lo, n.data))
                continue
            return False

    return True


root = BSTNode(80)
root.left = BSTNode(60)
root.right = BSTNode(160)
root.right.right = BSTNode(180)
print(is_bst(root))
print(is_bst_bfs(root))
root.right.left = BSTNode(190)
print(is_bst(root))
print(is_bst_bfs(root))


def reconstruct_bst_from_preorder(pre):
    def helper(pre, start, end):
        if len(pre) == 0 or end <= start:
            return None

        left_subtree_size = 0
        while left_subtree_size + start + 1 < len(pre) and \
                pre[left_subtree_size + start + 1] < pre[start]:
            left_subtree_size += 1

        return BSTNode(pre[start],
                       helper(pre, start + 1, start + 1 + left_subtree_size),
                       helper(pre, start + 1 + left_subtree_size, end))

    return helper(pre, 0, len(pre))


def rebuild_bst_from_preorder(pre):
    def helper(lower, upper):
        if root_idx[0] == len(pre):
            return None

        root = pre[root_idx[0]]

        if not lower <= root <= upper:
            return None

        root_idx[0] += 1
        left_subtree = helper(lower, root)
        right_subtree = helper(root, upper)
        return BSTNode(root, left_subtree, right_subtree)

    root_idx = [0]
    return helper(float('-inf'), float('inf'))


n = rebuild_bst_from_preorder([1, -1, 2, 3])
print(is_bst(n))
n = rebuild_bst_from_preorder([1, -1, 3])
print(is_bst(n))
n = rebuild_bst_from_preorder([1, 3])
print(is_bst(n))
n = rebuild_bst_from_preorder([1, -6, -1, 3, 2])
print(is_bst(n))
print(n.left.data, n.right.data, n.data)

import heapq


class IterTuple:
    def __init__(self, data, iter):
        self.data = data
        self.iter = iter

    def __lt__(self, other):
        return self.data < other.data


a1 = iter([5, 10, 15])
a2 = iter([3, 6, 9, 12, 15])
a3 = iter([8, 16, 24])

h = [IterTuple(next(i), i) for i in [a1, a2, a3]]
heapq.heapify(h)


def min_interval(h):
    min_dist = float('inf')
    nodes = (-1, -1, -1)

    while True:
        it = heapq.heappop(h)
        it2 = max(h)
        if it2.data - it.data < min_dist:
            min_dist = it2.data - it.data
            nodes = (it.data, h[0].data, h[1].data)

        it.data = next(it.iter, None)
        if it.data is None:
            break
        heapq.heappush(h, it)

    return min_dist, nodes


print(min_interval(h))


def build_bst(nums):
    def helper(start, end):
        if end <= start:
            return None

        mid = start + (end - start) // 2
        return BSTNode(nums[mid], helper(start, mid), helper(mid + 1, end))

    return helper(0, len(nums))


print(build_bst([1, 2, 3]).right.data)


def in_range(root, start, end):
    def helper(root, s, e):
        if root is None:
            return
        if e < start or s > end:
            return

        if s <= root.data <= e:
            subset.append(root.data)
            helper(root.left, s, root.data)
            helper(root.right, root.data, e)
        elif root.data < s:
            helper(root.right, s, e)
        elif root.data > e:
            helper(root.left, s, e)

    subset = []
    helper(root, start, end)
    return subset


root = BSTNode(19,
               BSTNode(7,
                       BSTNode(3,
                               BSTNode(2),
                               BSTNode(5)
                               ),
                       BSTNode(11,
                               None,
                               BSTNode(17, BSTNode(13))
                               )
                       ),
               BSTNode(43,
                       BSTNode(23,
                               None,
                               BSTNode(37,
                                       BSTNode(29,
                                               None,
                                               BSTNode(31)
                                               ),
                                       BSTNode(41)
                                       )
                               ),
                       BSTNode(47, None, BSTNode(53)))
               )
print(is_bst(root))
print(in_range(root, 16, 31))
