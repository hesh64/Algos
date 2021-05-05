def rpn_evaluator(string):
    ops = {
        '+': lambda x, y: x + y, '-': lambda x, y: x - y,
        '*': lambda x, y: x * y, '/': lambda x, y: x / y
    }
    exps = string.split(',')
    exps.reverse()
    print(exps)

    while len(exps) > 1:
        a, b, c = exps.pop(), exps.pop(), exps.pop()
        exps.append(ops[c](int(a), int(b)))

    return exps.pop()


print(rpn_evaluator('1,2,+'))
print(rpn_evaluator('3,4,+,2,*,1,+'))


def is_well_formed_string(string):
    stack = []
    opening = ['[', '{', '(']
    for c in string:
        if c in opening:
            stack.append(c)
        else:
            if c == ']' and len(stack) and stack[-1] == '[':
                stack.pop()
            elif c == '}' and len(stack) and stack[-1] == '{':
                stack.pop()
            elif c == ')' and len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(is_well_formed_string('(([]))'))
print(is_well_formed_string('(([]))()'))
print(is_well_formed_string('(([[]))()'))


def path_resolver(string):
    path = string.split('/')
    resolved = []

    for p in path:
        if len(p):
            if p == '..':
                resolved.pop()
            elif p != '.':
                resolved.append(p)

    return '/' + '/'.join(resolved)


print(path_resolver('/user/../bin'))
print(path_resolver('/usr/lib/../bin/gcc'))
print(path_resolver('scripts//./../scripts/awkscripts/././'))


def can_see_the_sunset(b):
    can = [b[0]]
    for h in b[1:]:
        while len(can) and can[-1] < h:
            can.pop()
        can.append(h)
    return can


print(can_see_the_sunset([4, 2, 3, 2, 1]))

from collections import deque


class MaxQueue:
    def __init__(self):
        self.elements = deque()
        self.maxes = deque()

    def enqueue(self, item):
        self.elements.append(item)
        while len(self.maxes) and self.maxes[-1] < item:
            self.maxes.pop()
        self.maxes.append(item)

    def deque(self):
        if self.elements[0] == self.maxes[0]:
            item, _ = self.elements.popleft(), self.maxes.popleft()
            return item
        else:
            return self.elements.popleft()

    def max(self):
        return self.maxes[0]


my_max = MaxQueue()
my_max.enqueue(3)
my_max.enqueue(1)
my_max.enqueue(3)
my_max.enqueue(2)
my_max.enqueue(0)
print(my_max.elements)
print(my_max.maxes)

