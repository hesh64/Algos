"""
YEETTT

"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Linked:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)

        else:
            cur = self.head
            while cur.next:
                cur = cur.next

            cur.next = Node(val)

    def get_all(self):
        vals = []
        cur = self.head
        while cur and cur.next:
            vals.append(cur.val)
            cur = cur.next

        vals.append(cur.val)
        return vals

    def contains(self, val):
        cur = self.head
        while cur and cur.next:
            if cur.val == val:
                return True

        return False

    def _for_each(self, fn):
        cur = self.head
        count = 0
        while cur:
            fn(cur, count)
            cur = cur.next
            count += 1

    def sum(self):
        cur = self.head
        count = 0
        while cur:
            count += cur.val
            cur = cur.next

    def delete(self, val):
        cur = self.head
        if cur.val == val:
            self.head = cur.next
        else:
            while cur.next:
                if cur.next.val == val:
                    cur.next = cur.next.next
                    return True
                else:
                    cur = cur.next
            return False
        return True

    def reverse(self):
        prev = self.head
        cur = prev.next
        prev.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev


linked = Linked()
linked.insert(1)
linked.insert(2)
linked.insert(3)
linked.insert(4)
linked.insert(5)
print(linked.get_all())
print(linked.delete(2))
print(linked.get_all())
print(linked.delete(5))
print(linked.get_all())
print('---')
ll = Linked()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
print('$$$$$$$$')
ll.reverse()
print(ll.get_all())
print('$$$$$$$$')
# print(linked.get_all())

print('recursive linked list')


class LinkedListRecursive:
    def __init__(self):
        self.head = None

    def _insert(self, cur, val):
        if cur.next is None:
            cur.next = Node(val)
            return
        else:
            return self._insert(cur.next, val)

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            return

        return self._insert(self.head, val)

    def _contains(self, cur, val):
        if cur:
            if cur.val == val:
                return True
            else:
                return self._contains(cur.next, val)
        else:
            return False

    def contains(self, val):
        return self._contains(self.head, val)

    def _for_each(self, head, num, fn):
        if head is None:
            return
        else:
            fn(head, num)
            self._for_each(head.next, num + 1, fn)

    def for_each(self, fn):
        return self._for_each(self.head, 0, fn)

    def _sum(self, cur):
        if cur is None:
            return 0

        return cur.val + self._sum(cur.next)

    def sum(self):
        return self._sum(self.head)

    def _delete(self, cur, val):
        if cur.next and cur.next.val == val:
            cur.next = cur.next.next
            return True
        elif cur.next:
            return self._delete(cur.next, val)

        return False

    def delete(self, val):
        if self.head.val == val:
            self.head = self.head.next
            return True
        else:
            return self._delete(self.head, val)

    def _reverse(self, cur, prev=None):
        if cur:
            next = cur.next
            cur.next = prev
            return self._reverse(next, cur)
        else:
            return prev

    def reverse(self, ):
        self.head = self._reverse(self.head, None)


llr = LinkedListRecursive()

llr.insert(1)
llr.insert(2)
llr.insert(3)
llr.insert(4)
llr.insert(5)

llr.reverse()
llr.for_each(lambda node, i: print(node.val))

print(llr.contains(3))
print(llr.contains(4))
print('sum', llr.sum())

llr.for_each(lambda node, i: print(node.val))
llr.delete(1)
llr.delete(3)
llr.delete(5)
print('---')
llr.for_each(lambda node, i: print(node.val))
