class DoubleNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'({self.key}: {self.value})'


class DLL:
    def __init__(self):
        self.head = DoubleNode()
        self.tail = DoubleNode()

    def is_empty(self):
        return self.head.next is None and self.tail.prev is None

    def insert(self, key, val):
        if self.is_empty():
            print(22)

            node = DoubleNode(key, val)
            self.head.next = node
            node.prev = self.head
            # head <-> node

            self.tail.prev = node
            node.next = self.tail
            # head <-> node <-> tail
            return node
        else:
            print(34)
            prev = self.tail.prev
            node = DoubleNode(key, val)

            # connect prev to new
            prev.next = node
            node.prev = prev

            node = self.tail.prev
            node.next = self.tail

            print(self.head.next)
            print(self.head.next.next)

            return node

    def del_at_head(self):
        if not self.is_empty():
            node = self.head.next
            next = node.next
            node.next = None
            node.prev = None
            self.head = next
            next.prev = self.head
            return True
        return False

    def move_to_tail(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        node.prev = self.tail.prev
        node.next = self.tail

    def __len__(self):
        if self.is_empty:
            return 0

        count = 0
        cur = self.head.next
        while cur != self.tail:
            count += 1
            cur = cur.next
        return count

    def __repr__(self):
        s = 'head -> '
        cur = self.head.next
        while cur is not None and cur != self.tail:
            s += str(cur) + ' -> '
            cur = cur.next
        s += 'tail'
        return s


class LRUCache:
    def __init__(self, capacity: int):
        self.ll = DLL()
        self.hash = {}
        self.capacity = capacity
        self.used = 0

    def get(self, key: int) -> int:
        if key in self.hash:
            self.ll.move_to_tail(self.hash[key])
            return self.hash[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.ll.insert(key, value)
        self.hash[node.key] = node
        self.used += 1
        if self.used > self.capacity:
            self.ll.del_at_head()


def main():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    # cache.put(3, 2)

    print(cache.ll)


main()
