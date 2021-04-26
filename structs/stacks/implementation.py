class Stack:
    def __init__(self):
        self.stack_list = []

    # O(1)
    def is_empty(self):
        return self.size() == 0

    # O(1)
    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()

    # O(1)
    def push(self, ele):
        self.stack_list.append(ele)

    # O(1)
    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    # O(1
    def size(self):
        return len(self.stack_list)


class Queue:
    def __init__(self):
        self.queue_list = []

    # O(1)
    def is_empty(self):
        return len(self.queue_list) == 0

    # O(1)
    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    # O(1)
    def back(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    # O(1)
    def size(self):
        return len(self.queue_list)

    # O(1)
    def enqueue(self, ele):
        self.queue_list.append(ele)

    # O(n) because we implemented the queue using a list, if we used a
    # a linked list, we can optimize this to O(1)
    def dequeue(self):
        if self.is_empty():
            return None

        return self.queue_list.pop(0)


def main():
    my_stack = Stack()

    for i in range(10):
        my_stack.push(i)

    print(my_stack.top())
    print(my_stack.pop())
    print(my_stack.top())

# main()
