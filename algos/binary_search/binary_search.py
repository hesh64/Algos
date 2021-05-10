import collections
import bisect
from typing import *

Student = collections.namedtuple('Student', ('name', 'gpa'))


def comp_gpa(student: Student) -> (float, str):
    return -student.gpa, student.name


def search_student(students, target: Student,
                   comp_gpa: Callable[[Student], Tuple[float, str]]):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    print('i', i)
    return 0 <= i < len(students) and students[i] == target


def make_student(str, float):
    return Student(str, float)


students = [Student(name, gpa) for name, gpa in [('a', 2.5), ('b', 3.1), ('c', 3.5)]]
print(students)
i = search_student(students, students[0], comp_gpa)
print(i)


def first_first_occurrence(nums, k):
    l, h, last = 0, len(nums) - 1, -1

    while l <= h:
        m = l + (h - l) // 2
        if nums[m] >= k:
            if nums[m] == k:
                last = m
            h = m - 1
        else:
            l = m + 1

    return last


print(first_first_occurrence([-14, -10, 2, 108, 108, 234, 285, 285, 401], 108))
print(first_first_occurrence([-14, -10, 2, 108, 108, 234, 285, 285, 401], 285))
print(first_first_occurrence([-14, -10, 2, 108, 108, 234, 285, 285, 401], -1))
print(first_first_occurrence([-14, -10, 2, 108, 108, 234, 285, 285, 401], 401))
print(first_first_occurrence([-14, -10, 2, 108, 108, 234, 285, 285, 401], -14))


def find_num_at_index(nums):
    l, h = 0, len(nums) - 1

    while l <= h:
        m = l + (h - l) // 2

        if m == nums[m]:
            return m

        if m > nums[m]:
            l = m + 1
        else:
            h = m - 1

    return -1


print('\n\nfind_num_at_index')
print(find_num_at_index([-2, 0, 2, 3, 6, 7, 9]))
print(find_num_at_index([-2, 0, 2, 4, 6, 7, 9]))
print(find_num_at_index([-2, 0, 1, 3, 6, 7, 9]))
print(find_num_at_index([-2, 0, 1, 5, 6, 7, 9]))


def find_smallest_in_cyclic(nums):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < nums[hi]:
            hi = mid
        else:
            lo = mid + 1

    return nums[hi]


print('\n\nfind_smallest_in_cyclic')
print(find_smallest_in_cyclic([103, 203, 220, 234, 279, 368, 378, 478, 550, 631]))
print(find_smallest_in_cyclic([378, 478, 550, 631, 103, 203, 220, 234, 279, 368]))
print(find_smallest_in_cyclic([378, 478, 550, 631, 1030, 203, 220, 234, 279, 368]))
print(find_smallest_in_cyclic([378, 478, 550, 63, 103, 203, 220, 234, 279, 368]))
print(find_smallest_in_cyclic([378, 478, 55, 63, 103, 203, 220, 234, 279, 368]))
print(find_smallest_in_cyclic([378, 478, 550, 631, 1030, 2030, 220, 234, 279, 368]))


def sqrt(n):
    lo, hi = 0, n
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if mid * mid > n:
            hi = mid - 1
        elif mid * mid <= n:
            lo = mid + 1

    return lo - 1


print('\n\nsqrt', sqrt(100))
print('\n\nsqrt', sqrt(9))
print('\n\nsqrt', sqrt(1))
print('\n\nsqrt', sqrt(4))
print('\n\nsqrt', sqrt(64))
print('\n\nsqrt', sqrt(300))
