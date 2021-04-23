class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


def stringify(h):
    if h is not None:
        return str(h.data) + ' -> ' + stringify(h.next)
    return 'end'


def reverse(l, s, f):
    d = sh = ListNode(0, l)
    for _ in range(1, s):
        sh = sh.next

    si = sh.next
    for _ in range(f - s):
        tmp = si.next
        si.next = tmp.next
        tmp.next = sh.next
        sh.next = tmp

    return d.next


def has_cycle(h):
    def get_len(h):
        t, c = h, 0
        while True:
            t = t.next
            c += 1
            if t == h:
                return c

    slow, fast = h, h
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            cycle_it = h
            for _ in range(get_len(slow)):
                cycle_it = cycle_it.next

            it = h
            while it != cycle_it:
                it = it.next
                cycle_it = cycle_it.next

            return cycle_it

    return None


def has_cycle_without_measuring_cycle_length(h):
    slow = fast = h
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            slow = h
            while True:
                if slow == fast:
                    return slow
                slow = slow.next
                fast = fast.next
    return None


def find_overlapping(l, r):
    def get_len(l):
        i = 1
        t = l.next
        while t.next:
            t = t.next
            i += 1
        return i

    len_l = get_len(l)
    len_r = get_len(r)

    if len_l > len_r:
        for _ in range(len_l - len_r):
            l = l.next
    else:
        for _ in range(len_r - len_l):
            r = r.next

    while l != r:
        l = l.next
        r = r.next
        if l == r:
            return l

    return None


class DoubleNode:
    def __init__(self, key, data, prev=None, next=None):
        self.key = key
        self.data = data
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def push(self, key, value):
        n = DoubleNode(key, value)
        self.insert(n)
        return n

    def insert(self, n: DoubleNode):
        if self.head is None and self.tail is None:
            self.head = self.tail = n
            return self.head
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
            return n

    def remove(self, n: DoubleNode):
        if self.head is None:
            return

        if n is self.head:
            if self.head.next:
                self.head.next.prev = None
                next = self.head.next
                self.head.next = None
                self.head = next
            else:
                self.head = self.tail = None

        elif n is self.tail:
            if self.tail.prev:
                self.tail.prev.next = None
                prev = self.tail.prev
                self.tail.prev = None
                self.tail = prev

        else:
            prev = n.prev
            next = n.next
            prev.next = next
            next.prev = prev
            n.next = n.prev = None

    def move_to_tail(self, n: DoubleNode):
        self.remove(n)
        self.insert(n)

    def pop(self):
        if self.head is None:
            return None

        if self.head == self.tail:
            n = self.head
            self.head = self.tail = None
            return n.data
        else:
            n = self.head
            next = self.head.next
            self.head.next = None
            self.head = next
            self.head.prev = None
            return n

    def __repr__(self):
        tmp = self.head
        s = ''
        while tmp:
            s += str(tmp.data) + ' -> '
            tmp = tmp.next
        s += 'end'
        return s


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.ll = DoubleLinkedList()

    def __getitem__(self, item):
        if item == 'put':
            return lambda *x: self.put(*x)
        if item == 'get':
            return lambda *x: self.get(*x)

    def put(self, key, val):
        if key in self.cache:
            self.ll.move_to_tail(self.cache[key])
            self.cache[key].data = val
        else:
            self.cache[key] = self.ll.push(key, val)
            if len(self.cache) > self.capacity:
                node = self.ll.pop()
                data = node.data
                del self.cache[node.key]
                return data

    def get(self, key):
        if key in self.cache:
            self.ll.move_to_tail(self.cache[key])
            return self.cache[key].data

        return -1


def main():
    head = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2)))))
    print(stringify(head))
    reverse(head, 2, 4)
    print(stringify(head))

    tail = ListNode(2)
    head = ListNode(11, ListNode(3, ListNode(5, ListNode(7, tail))))
    tail.next = head.next.next
    print(has_cycle(head))
    print(has_cycle_without_measuring_cycle_length(head))

    l = ListNode(11, ListNode(3, ListNode(5, ListNode(7, ListNode(2)))))
    r = ListNode(13, ListNode(10, l.next.next.next))
    print(find_overlapping(l, r))

    print('---')
    # dl = DoubleLinkedList()
    # dl.push(1)
    # dl.push(2)
    # n = dl.push(3)
    # n = dl.push(31)
    # dl.push(311)

    # print(dl)
    # print(dl.pop())
    # print(dl.pop())
    # print(dl.pop())
    # print(dl.pop())
    # print(dl.pop())
    # # dl.move_to_tail(n)
    # print(dl)

    print('lru')
    lru = LRUCache(2)
    l1 = ["put", "put", "get", "put", "get", "put", "get", "get", "get"]
    l2 = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    res = [None, None, 1, None, -1, None, -1, 3, 4]
    for c, (i, j) in enumerate(zip(l1, l2)):
        # print(i, j)
        print(i, '(', j, ')', ':', lru[i](*j), res[c])
        print('returned')


main()
