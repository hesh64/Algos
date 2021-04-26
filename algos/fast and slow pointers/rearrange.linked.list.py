class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


"""
Rearrange a LinkedList (medium) #
Given the head of a Singly LinkedList, write a method to modify the LinkedList such that
the nodes from the second half of the LinkedList are inserted alternately to the nodes from
the first half in reverse order. So if the LinkedList has nodes
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

"""


def get_half(head):
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


def reverse(head):
    old = head
    new_head = old.next
    old.next = None
    temp = new_head.next
    new_head.next = old
    while temp:
        old = new_head
        new_head = temp
        temp = temp.next
        new_head.next = old

    return new_head


def rearrange(head):
    half = get_half(head)
    half_reversed = reverse(half)
    first_half = head

    while half_reversed:
        temp = first_half.next
        first_half.next = half_reversed
        half_reversed = half_reversed.next
        first_half.next = temp
        first_half = first_half

    return head


def main():
    # rearrange()

    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(4)
    node.next.next.next.next = Node(5)

    n = rearrange(node)
    print(n.value)
    print(n.next.value)


main()
