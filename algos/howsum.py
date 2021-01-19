def how_sum(target, nums):
    if target == 0:
        return []

    if target < 0:
        return False

    for num in nums:
        rem = target - num
        res = how_sum(rem, nums)
        if res != False:
            res.append(num)
            return res

    return False


def how_sum(target, nums, memo=dict()):
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return False

    for num in nums:
        rem = target - num
        memo[rem] = how_sum(rem, nums)
        if memo[rem] != False:
            memo[rem].append(num)
            return res

    return False


print(how_sum(7, [4, 3, 5]))
