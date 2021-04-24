import heapq


class Node:
    def __init__(self, key, data, prev=None, next=None):
        self.key = key
        self.data = data
        self.freq = 1
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'(key={self.key}, freq={self.freq})'

    def __lt__(self, other):
        return self.freq < other.freq


class DoubleLinkedList:
    def __init__(self):
        self.head: Node = Node(-1, -1)
        self.tail: Node = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self):
        return self.head.next == self.tail

    def remove(self, n: Node):
        if n == self.tail or n == self.head:
            return

        n.prev.next = n.next
        n.next.prev = n.prev
        n.prev = None
        n.next = None

    def add_to_tail(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def push(self, key, val):
        n = Node(key, val)
        self.add_to_tail(n)
        return n

    def pop(self):
        if self.head.next != self.tail:
            n = self.head
            self.head.next.prev = self.head
            self.head = self.head.next
            n.prev = None
            n.next = None
            return n
        return None

    def min(self):
        n = None
        tmp = self.head.next

        while tmp and tmp != self.tail:
            if n is None:
                n = tmp
            elif n.freq > tmp.freq:
                n = tmp

            tmp = tmp.next

        return n

    def __repr__(self):
        tmp = self.head.next
        s = 'head -> '
        while tmp and tmp != self.tail:
            s += str(tmp) + ' -> '
            tmp = tmp.next
        s += 'tail'
        return s


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.list = DoubleLinkedList()

    def put(self, key, val):
        if self.capacity == 0:
            return

        if key not in self.cache:
            if len(self.cache) == self.capacity:
                min_node = self.list.min()
                self.list.remove(min_node)
                del self.cache[min_node.key]
                # print('popped min:', min_node)

            self.cache[key] = self.list.push(key, val)

        else:
            self.cache[key].freq += 1
            self.cache[key].data = val

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.list.remove(node)
        node.freq += 1
        self.list.add_to_tail(node)

        return node.data

    def __getitem__(self, item):
        if item == 'put':
            return lambda *x: self.put(*x)

        if item == 'get':
            return lambda *x: self.get(*x)

    def __repr__(self):
        return f"""{self.cache}
{self.list}"""


def main():
    lfu = LFUCache(1)
    print(None, lfu.put(2, 1), lfu.get(2), lfu.put(3, 2), lfu.get(2), lfu.get(3))
    lfu = LFUCache(2)
    print(None, lfu.put(1, 1), lfu.put(2, 2), lfu.get(1), lfu.put(3, 3), lfu.get(2), lfu.get(3), lfu.put(4, 4),
          lfu.get(1), lfu.get(3), lfu.get(4))
    lfu = LFUCache(3)
    print(None, lfu.put(2, 2), lfu.put(1, 1), lfu.get(2), lfu.get(1), lfu.get(2), lfu.put(3, 3), lfu.put(4, 4),
          lfu.get(3), lfu.get(2), lfu.get(1), lfu.get(4))

    lfu = LFUCache(2)
    print(None, lfu.put(3, 1), lfu.put(2, 1), lfu.put(2, 2), lfu.put(4, 4), lfu.get(2))

    lfu = LFUCache(0)
    print(lfu.put(0, 0), lfu.get(0))

    # print('\ntest case 2 LFU(size=3)')
    # l1 = ["put", "put", "get", "get", "get", "put", "put", "get", "get", "get", "get"]
    # l2 = [[2, 2], [1, 1], [2], [1], [2], [3, 3], [4, 4], [3], [2], [1], [4]]
    # lfu = LFUCache(3)
    # res = [None, None, 2, 1, 2, None, None, -1, 2, 1, 4]
    #
    # for c, (i, j) in enumerate(zip(l1, l2)):
    #     print(f'{i}({j}) ->', end=' ')
    #     print(lfu[i](*j), f'expected: {res[c]}')
    #     print(lfu.list, '\n')
    return
    print('\ntest case 3 LFU(size=1)')
    l1 = ["put", "get", "put", "get", "get"]
    l2 = [[2, 1], [2], [3, 2], [2], [3]]
    lfu = LFUCache(1)
    res = [None, 1, None, -1, 2]

    for c, (i, j) in enumerate(zip(l1, l2)):
        print(f'calling... {i}({j})', lfu[i](*j), res[c])
        print(lfu.list, '\n')

    # lfu = LFUCache(3)
    # lfu.put(2, 2)
    # lfu.put(1, 1)
    # print(lfu.get(2))


main()
