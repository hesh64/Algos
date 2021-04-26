class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


def reverse_every_k_elements(head, k):
    new_head = None
    i = 1

    start = head
    cur = start

    while cur and i < k:
        cur = cur.next
        i += 1

    next = cur.next

    cur.next = start
    if new_head is None:
        new_head = cur

    cur = cur.next
    cur.next = None
    print(new_head)

    # cur.next = start
    # # print(cur.next.val)
    # start = cur
    # cur = cur.next
    # cur.next = next
    #
    # print(cur.val)

    if new_head is None:
        new_head = start

    return new_head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    result = reverse_every_k_elements(head, 3)

    print(result)


main()
