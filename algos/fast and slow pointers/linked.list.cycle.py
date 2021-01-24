class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow = head
    fast = head

    while slow and fast:
        if not slow.next:
            break

        if not fast.next or not fast.next.next:
            break

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


"""
Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.
"""


def cycle_length(head):
    slow = head
    fast = head

    while slow and fast:
        if not slow.next:
            break

        if not fast.next or not fast.next.next:
            break

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            itr = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                itr += 1

            return itr

    return False


def where_the_cycle_begins(head):
    k = cycle_length(head)

    slow, fast = head, head

    for i in range(k):
        fast = fast.next

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast.value


"""
Problem Statement #
Any number will be called a happy number if, after repeatedly replacing it with a
number equal to the sum of the square of all of its digits, leads us to number ‘1’.
All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck
in a cycle of numbers which does not include ‘1’.
"""


# do this with a linked list for some reason? No thanks.
def happy_number(num):
    digits = [int(x) for x in str(num)]
    while len(digits) > 1:
        tmp = digits[0] ** 2 + digits[1] ** 2
        digits = [int(x) for x in str(tmp)]
    if digits[0] == 1:
        return True

    return False


def middle_of_linked_list(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


"""
Palindrome LinkedList (medium) #
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be
 in the original form once the algorithm is finished. The algorithm should have O(N) 
 time complexity where ‘N’ is the number of nodes in the LinkedList.

"""


def is_palindrome(head):
    # check this out
    # let's make it to the end
    first = head

    def jump_to_end(node):
        # reference the outside world
        nonlocal first
        # as long as there is a node and as long
        # as i am not past the half way point
        # tail will be True or False, node will be
        # the right half of the linked list and first
        # will be the the left half. Dive to the end useing
        # recursion and as you unwind the stack move first to
        # first.next and return that boolean result
        # print(node.value)
        if node:
            tail = jump_to_end(node.next)
            if node == first:
                return tail
            if tail is not None:
                comp = first.value == node.value
                first = first.next
                return comp and tail
            else:
                comp = first.value == node.value
                first = first.next
                return comp

    res = jump_to_end(head)
    return res


# we can get the length first and then automate the flag
# but for purpose of practice this will do
def is_palindrome_stack_q(head, odd=True):
    stack = []
    slow = head
    fast = head

    while fast and fast.next:
        stack.insert(0, slow)
        slow = slow.next
        fast = fast.next.next

    if odd:
        slow = slow.next

    while slow:
        if len(stack):
            top = stack.pop(0)
            if top.value != slow.value:
                return False
            else:
                slow = slow.next
        else:
            return False

    return True


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))
    print("Middle of LinkedList: " + str(middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
    k = cycle_length(head)
    print('Cycle length is:', k)
    print('Where do they split?', where_the_cycle_begins(head))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    print(happy_number(23))

    palindrome = Node(1)
    palindrome.next = Node(2)
    palindrome.next.next = Node(3)
    palindrome.next.next.next = Node(2)
    palindrome.next.next.next.next = Node(1)
    print('Is 12321 a palindrome?', is_palindrome(palindrome))
    print('Is 12321 a palindrome stack?', is_palindrome_stack_q(palindrome))

    palindrome = Node(1)
    palindrome.next = Node(2)
    palindrome.next.next = Node(3)
    palindrome.next.next.next = Node(3)
    palindrome.next.next.next.next = Node(2)
    palindrome.next.next.next.next.next = Node(1)
    print('Is 123321 a palindrome?', is_palindrome(palindrome))
    print('Is 123321 a palindrome stack?', is_palindrome_stack_q(palindrome, odd=False))

    palindrome = Node(1)
    palindrome.next = Node(2)
    palindrome.next.next = Node(5)
    palindrome.next.next.next = Node(3)
    palindrome.next.next.next.next = Node(2)
    palindrome.next.next.next.next.next = Node(1)
    print('Is 125321 a palindrome?', is_palindrome(palindrome))

    palindrome = Node(2)
    palindrome.next = Node(2)
    palindrome.next.next = Node(5)
    palindrome.next.next.next = Node(3)
    palindrome.next.next.next.next = Node(2)
    palindrome.next.next.next.next.next = Node(1)
    print('Is 125321 a palindrome?', is_palindrome(palindrome))


main()
