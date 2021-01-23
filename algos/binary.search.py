def binary(x, nums):
    s, e = 0, len(nums) - 1

    while s <= e:
        mid = (s + e) // 2
        print(nums[mid], x)

        if nums[mid] == x:
            return mid

        if nums[mid] < x:
            s = mid + 1

        else:
            e = mid - 1

    return -1


n = [1, 2, 3, 4, 5]

print(binary(9, [-1,0,3,5,9,12]))


# def binary_pivot(nums):
#     s, e = 0, len(nums) - 1
#
#     print(s, e)
#
#     while s <= e:
#         print(s)
#         mid = (s + e) // 2
#
#         if nums[mid] > nums[mid + 1]:
#             return mid
#
#         if nums[mid] < nums[mid + 1]:
#             s = mid + 1
#
#         else:
#             e = mid - 1
#
#     return -1
#
#
# n_p = [3, 4, 5, 1, 2]
#
# print(binary_pivot(n_p))
