class Interval:
    def __init__(self, start, end, start_closed=False, end_closed=False):
        self.start = start
        self.end = end
        self.start_closed = start_closed
        self.end_closed = end_closed

    def __repr__(self):
        str = ''
        if self.start_closed:
            str += '['
        else:
            str += '('
        str += f'{self.start}, {self.end}'
        if self.end_closed:
            str += ']'
        else:
            str += ')'

        return str

    def __lt__(self, other):
        return self.start < other.start

    def copy_constructor(self):
        return Interval(self.start, self.end, self.start_closed, self.end_closed)


intervals = [Interval(1, 1, True, True), Interval(0, 3), Interval(2, 4, True, True), Interval(3, 4, True),
             Interval(5, 7, True, False), Interval(7, 8, True, False), Interval(8, 11, True, False),
             Interval(9, 11, False, True), Interval(13, 15), Interval(12, 16, False, True),
             Interval(12, 14, True, True),
             Interval(16, 17)]


def join_intervals(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda x: x.start)
    x = intervals[0].copy_constructor()

    merged = []
    for i in range(len(intervals)):
        y = intervals[i]
        if x.end < y.start:
            merged.append(x)
            x = y.copy_constructor()

        else:
            start_closed = False
            end_closed = False
            if (x.start == y.start and (x.start_closed or y.start_closed)) \
                    or (x.start < y.start and x.start_closed is True) or (y.start < x.start and y.start_closed is True):
                start_closed = True

            if (x.end == y.end and (x.end_closed or y.end_closed)) \
                    or (x.end < y.end and y.end_closed is True) or (y.end < x.end and x.end_closed is True):
                end_closed = True

            x.end = max(x.end, y.end)
            x.start_closed, x.end_closed = start_closed, end_closed

    merged.append(x)
    return merged


print(join_intervals(intervals))


class Node:
    def __init__(self, key, data, left=None, right=None):
        self.key, self.data, self.left, self.right = key, [data], left, right

    def append(self, value):
        self.data.append(value)

    def __repr__(self):
        return f'{self.key}: {[str(d) for d in self.data]}'


class Counter:
    def __init__(self):
        self.head = None

    def insert(self, key, val):
        if self.head is None:
            self.head = Node(key, val)
            return

        cur = self.head
        while cur:
            if cur.key == key:
                cur.append(val)
                return
            if cur.key < key:
                if not cur.right:
                    cur.right = Node(key, val)
                    return

                cur = cur.right

            elif cur.key > key:
                if not cur.left:
                    cur.left = Node(key, val)
                    return
                cur = cur.left

    def in_order(self):
        objects = []
        stack = [(self.head, False)]

        while stack:
            node, is_finished = stack.pop()
            if node:
                if not is_finished:
                    stack.extend([(node.right, False), (node, True), (node.left, False)])
                else:
                    objects.append(node.data)

        return objects


import random

random.seed(42)


class Student:
    def __init__(self, age):
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return f'Student({self.age})'


students = [Student(random.randint(6, 16)) for _ in range(50)]
counter = Counter()
for student in students:
    counter.insert(student.age, student)

print(counter.in_order())

from collections import Counter
import random

random.seed(42)


class Student:
    def __init__(self, age):
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return f'Student({self.age})'


students = [Student(random.randint(6, 16)) for _ in range(10)]


def sort_students(students):
    age_to_count = Counter((s.age for s in students))
    age_to_offset, offset = {}, 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count

    # print(age_to_count)
    # print(age_to_offset)
    while age_to_offset:
        print(age_to_offset)
        from_age = next(iter(age_to_offset))
        print(age_to_offset)
        # print(from_age)
        from_idx = age_to_offset[from_age]

        to_age = students[from_idx].age
        to_idx = age_to_offset[students[from_idx].age]
        students[from_idx], students[to_idx] = students[to_idx], students[from_idx]
        age_to_count[to_age] -= 1

        if age_to_count[to_age]:
            age_to_offset[to_age] = to_idx + 1
        else:
            del age_to_offset[to_age]

    print(students)


sort_students(students)
