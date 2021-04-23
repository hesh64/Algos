import bisect
from collections import namedtuple
from typing import List

Student = namedtuple('Student', ('name', 'grade_point_average'))


def comp_gpa(student: Student):
    return (-student.grade_point_average, student.name)


def search_student(students: List[Student], target: Student):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target


def search_fist_occurrence(arr, k):
    s, e, last = 0, len(arr) - 1, -1

    while s <= e:
        mid = s + (e - s) // 2

        if arr[mid] == k:
            last = mid
            e = mid - 1
        elif arr[mid] < k:
            s = mid + 1
        else:
            e = mid - 1

    return last


def search_first_ele_lt(arr, k):
    s, e, last = 0, len(arr) - 1, -1
    while s <= e:
        mid = s + (e - s) // 2
        if arr[mid] <= k:
            s = mid + 1
        else:
            last = mid
            e = mid - 1

    return last


def find_ele_eq_index(arr):
    s, e = 0, len(arr) - 1

    while s <= e:
        mid = s + (e - s) // 2

        if mid > arr[mid]:
            s = mid + 1
        elif mid < arr[mid]:
            e = mid - 1
        else:
            return mid

    return -1


def search_cyclic_array(arr, t):
    s, e = 0, len(arr) - 1
    while s <= e:
        mid = s + (e - s) // 2

        if arr[mid] == t:
            return mid

        if arr[mid] <= arr[e] and t >= arr[mid]:
            s = mid + 1
        elif arr[mid] <= arr[e] and t <= arr[mid]:
            e = mid - 1

        elif arr[s] <= arr[mid] and t <= arr[mid]:
            e = mid - 1
        elif arr[s] <= arr[mid] and t >= arr[mid]:
            s = mid + 1

    return -1


def main():
    arr = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    print(search_fist_occurrence(arr, 108))
    print(search_fist_occurrence(arr, 285))
    print(search_fist_occurrence(arr, 401))
    print(search_fist_occurrence(arr, -14))
    print(search_fist_occurrence(arr, -1))
    print(search_fist_occurrence(arr, 243))

    print('\nsearch_first_ele_lt')
    print(search_first_ele_lt(arr, -1))
    print(search_first_ele_lt(arr, 108))
    print(search_first_ele_lt(arr, 1080))

    print('\nele eq index')
    print(find_ele_eq_index(arr))
    arr = [0, 2, 3, 4, 5]
    print(find_ele_eq_index(arr))
    arr = [-1, 0, 1, 2, 4]
    print(find_ele_eq_index(arr))

    arr = [8] * 8
    print('\nsearch_fist_occurrence')
    print(search_fist_occurrence(arr, 8))

    print('\nsearch_cyclic_array')
    arr = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
    print(search_cyclic_array(arr, 631))
    print(search_cyclic_array(arr, 378))
    print(search_cyclic_array(arr, 279))


main()
