# O(n*log(n) + O(n^2))
def search_triplets(nums):
    # O(n*log(n))
    nums.sort()
    triplets = []
    # O(n ^ 2)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # O(n)
        search_pair(nums, -nums[i], i + 1, triplets)

    return triplets


# O(n)
def search_pair(nums, target, left, triplet):
    right = len(nums) - 1

    # total of O(n)
    while left < right:
        pair = nums[left] + nums[right]

        if pair == target:
            triplet.append([nums[left], nums[right], -target])

            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1

        elif target > pair:
            left += 1
        else:
            right -= 1


from collections import deque


# O(n/2)
def square_nums(nums):
    left, right = 0, len(nums) - 1
    new_list = [None] * len(nums)
    cursor = len(new_list) - 1
    while left <= right:
        lq, rq = nums[left] ** 2, nums[right] ** 2

        if lq > rq:
            new_list[cursor] = lq
            left += 1
        else:
            new_list[cursor] = rq
            right -= 1

        cursor -= 1

    return new_list


def main():
    nums = [-5, 2, -1, -2, 3]
    result = search_triplets(nums)
    print(result)

    nums = [-4, -1, 0, 3, 10]
    print(square_nums(nums))
    nums = [-5, -3, -2, -1]
    print(square_nums(nums))


main()
