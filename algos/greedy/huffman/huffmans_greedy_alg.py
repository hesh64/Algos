import heapq


class TreeNode:
    def __init__(self, left=None, right=None):
        self.left, self.right = left, right

    def nodes(self):
        return (self.left, self.right)

    def __repr__(self):
        return f'({self.left}) ({self.right})'


def freq_counter(string):
    freq = {}
    for c in string:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1

    items = [[v, k] for k, v in freq.items()]
    heapq.heapify(items)
    return items


# O(nlog(n))
def huffman_alg(string):
    heap = freq_counter(string)

    # O(n)
    while len(heap) > 1:
        # min1
        left = heapq.heappop(heap)
        # min1 < min2
        right = heapq.heappop(heap)

        #    ()
        #   /  \
        # min1 min2
        # ----> heap O(log(n))
        heapq.heappush(heap, [left[0] + right[0], TreeNode(left[1], right[1])])

    return heap[0][1]


def helper(root, cur):
    if root is None:
        return

    if type(root) is str:
        print(root, ''.join(cur))
        return

    else:
        cur.append('0')
        helper(root.left, cur)
        cur.pop()

        cur.append('1')
        helper(root.right, cur)
        cur.pop()
        return


if __name__ == '__main__':
    string = 'BCAADDDCCACACAC'
    head = huffman_alg(string)
    print(head)
    helper(head, [])

    print('\n')
    string = (5 * 'D') + (60 * 'A') + (10 * 'C') + (25 * 'B')
    head = huffman_alg(string)
    print(head)
    helper(head, [])

    print('\n')
    string = (3 * 'A') + (2 * 'B') + ('C' * 6) + ('D' * 8) + ('E' * 2) + ('F' * 6)
    head = huffman_alg(string)
    print(head)
    helper(head, [])
