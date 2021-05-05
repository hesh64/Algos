class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next

    def __repr__(self):
        return f'{self.data}'


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))


def print_list(head):
    lst = []
    while head:
        lst.append(str(head))
        head = head.next
    return lst


print(print_list(head))


def reverse(h, s, f):
    dummy = Node(-1, h)

    for _ in range(1, s):
        dummy = dummy.next

    cur = dummy.next
    for _ in range(f - s):
        next = cur.next
        cur.next = next.next
        next.next = dummy.next
        dummy.next = next

    return head


print('\n')
print(print_list(reverse(head, 2, 4)))

head = Node(1, Node(2))
three = Node(3)
head.next.next = three
four = Node(4, Node(5))
three.next = four
four.next.next = three
cur = head


def find_cycle(ll):
    if ll is None or ll.next is None:
        return None
    slow, fast = ll, ll
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if slow != fast:
        return None

    i = 0
    while True:
        fast = fast.next
        i += 1
        if slow == fast:
            break

    slow, fast = head, head
    for _ in range(i):
        fast = fast.next
    while slow != fast:
        slow, fast = slow.next, fast.next

    return slow


print(find_cycle(head))

print('\n\n')

tail = Node('x', Node('y', Node('z')))
l1 = Node('h', Node('i'))
l2 = Node('m')

l1.next.next = tail
l2.next = tail

print(print_list(l1))


def get_length(l1):
    c = 0
    while l1:
        c += 1
        l1 = l1.next

    return c


def find_convergence(l1, l2):
    l1_length = get_length(l1)
    l2_length = get_length(l2)

    while l1_length > l2_length:
        l1 = l1.next
        l1_length -= 1

    while l2_length < l2_length:
        l2 = l2.next
        l2_length -= 1

    while l1 and l2:
        if l1 == l2:
            return l1
        l1, l2 = l1.next, l2.next

    return None


print(find_convergence(l1, l2))

tail = Node('z', Node('y', Node('x')))
l1 = Node('h', Node('i'))
l2 = Node('m')
tail.next.next.next = tail

l1.next.next = tail
l2.next = tail


def find_converged_node_in_cyclic(l1, l2):
    def has_cycle(l):
        slow, fast = l, l
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow == fast:
                return True

        return False

    l1_has_cycle = has_cycle(l1)
    l2_has_cycle = has_cycle(l2)
    if (l1_has_cycle is False and l2_has_cycle is True) \
            or (l1_has_cycle is True and l2_has_cycle is False):
        return None

    if l1_has_cycle is False and l2_has_cycle is False:
        return find_convergence(l1, l2)

    slow_l1, fast_l2 = l1, l2
    while True:
        slow_l1 = slow_l1.next
        fast_l2 = fast_l2.next.next
        if slow_l1 == fast_l2:
            return slow_l1


print(find_converged_node_in_cyclic(l1, l2))
