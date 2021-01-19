# time O(n^2)
# space
def sum(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    return nums[0] + sum(nums[1:])


assert sum([]) == 0, 'sum([])'
assert sum([1]) == 1, 'sum([1])'
assert sum([1, 5, 7]) == 13, 'sum([1,5,7])'

'''
    a little more efficient
    
    O(n)
'''
def sum_idx_helper(nums, idx, l):
    if l == 0:
        return 0

    if idx + 1 == l:
        return nums[idx]

    return nums[idx] + sum_idx_helper(nums, idx + 1, l)


def sum_idx(nums):
    return sum_idx_helper(nums, 0, len(nums))


assert sum_idx([]) == 0, 'sum_idx([])'
assert sum_idx([1]) == 1, 'sum_idx([1])'
assert sum_idx([1, 5, 7]) == 13, 'sum_idx([1,5,7])'
