arr = [3, 4, 5, 0, 2]


def partition_even_odd(arr):
    even, odd = 0, len(arr) - 1
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[even], arr[i] = arr[i], arr[even]
            even += 1

    return arr


print(partition_even_odd(arr))

arr = [0, 1, 2, 0, 2, 1, 1]


def dutch_national_problem(arr):
    lo, hi = 0, len(arr) - 1
    i = 0
    while i <= hi:
        if arr[i] == 0:
            arr[lo], arr[i] = arr[i], arr[lo]
            lo += 1
        elif arr[i] == 2:
            arr[hi], arr[i] = arr[i], arr[hi]
            hi -= 1

        i += 1


dutch_national_problem(arr)
print(arr)


def add_one(arr):
    # n
    arr.reverse()
    i, car = 0, 1
    # n
    while i < len(arr) and car > 0:
        arr[i] += car
        car = 0

        if arr[i] > 9:
            car = 1
            arr[i] %= 10
        i += 1

    if car != 0:
        arr.append(1)

    # n
    arr.reverse()
    return arr


# 3n -> oN

arr = [9, 9]
add_one(arr)
add_one(arr)
print(arr)

from functools import lru_cache


# this works sure.. but there is a simpler approach
def take_steps(arr):
    @lru_cache(None)
    def helper(start):
        nonlocal arr
        if start >= len(arr):
            return False

        if start == len(arr) - 1:
            return True

        return any(helper(start + i) for i in range(1, arr[start] + 1))

    return helper(0)


print('\ntake_steps:')
print(take_steps([3, 3, 1, 0, 2, 0, 1]))
print(take_steps([3, 3, 1, 0, 1, 0, 1]))
print(take_steps([1, 3, 1, 0, 1, 0, 1]))
print(take_steps([1, 3, 1, 2, 1, 0, 1]))
print(take_steps([1, 3, 1, 0, 2, 0, 1]))


def steps(a):
    max_dist, i, end = a[0], 0, len(a) - 1
    while i <= max_dist < end:
        max_dist = max(i + a[i], max_dist)
        i += 1
    return max_dist >= end


print('\nsteps:')
print(steps([3, 3, 1, 0, 2, 0, 1]))
print(steps([3, 3, 1, 0, 1, 0, 1]))
print(steps([1, 3, 1, 0, 1, 0, 1]))
print(steps([1, 3, 1, 2, 1, 0, 1]))
print(steps([1, 3, 1, 0, 2, 0, 1]))


def copy_duplicates(a):
    p = 0
    for i in range(len(a)):
        if a[p] != a[i]:
            p += 1
            a[p] = a[i]
    return p + 1


a = [1, 2, 2, 3, 4, 5, 5, 5, 6]
end = copy_duplicates(a)
print(a[:end])


def stock_profit(a):
    if len(a) <= 1:
        return 0

    gp, lc = 0, a[0]

    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            lc = a[i]
        gp = max(gp, a[i] - lc)

    return gp


a = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(stock_profit(a))

a = [310, 310]
print(stock_profit(a))

a = [3120, 310, 0]
print(stock_profit(a))

a = [3120, 11310, 0]
print(stock_profit(a))


def buy_sell_stocks_twice(prices):
    min_price = float('inf')
    profits = []
    for price in prices:
        min_price = min(min_price, price)
        profits.append(max(0, price - min_price))

    max_price = float('-inf')
    max_sell = 0

    for i in range(len(prices) - 1, 0, -1):
        max_price = max(prices[i], max_price)
        max_sell = max(max_sell, max_price - prices[i] + profits[i - 1])

    return max_sell


print('\nbuy_sell_stocks_twice')
print(buy_sell_stocks_twice([12, 11, 13, 9, 12, 8, 14, 13, 15]))


# rearrange an array such that for a1, a2, ..., an
# a1 <= a2 >= a3 <= a4 >= a5....
# O(lg n)
def rearrange(a):
    a.sort()
    for i in range(1, len(a), 2):
        if i + 1 < len(a):
            a[i], a[i + 1] = a[i + 1], a[i]


a = [1, 2, 3, 4, 5, 6, 7]
rearrange(a)
print(a)


# O(n)
def rearrange2(a):
    for i in range(len(a)):
        a[i: i + 2] = sorted(a[i: i + 2], reverse=bool(i % 2))


a = [1, 2, 3, 4, 5, 6, 7]
rearrange2(a)
print(a)

print('\npermutations')


def next_permutation(a):
    if len(a) == 0:
        return []

    end = len(a) - 2
    while end >= 0 and a[end] > a[end + 1]:
        end -= 1

    if end == -1:
        return []

    # print(a[end], a[end + 1:])
    swap_index = len(a) - 1
    for i in range(len(a) - 1, end, -1):
        # print(a[i], a[end])
        if a[i] > a[end]:
            swap_index = i
            break
    # print(a)
    a[end], a[swap_index] = a[swap_index], a[end]
    # print(a)
    a[end + 1:] = reversed(a[end + 1:])

    return a


a = [6, 2, 1, 5, 4, 3, 0]
print(next_permutation(a))

a = [3, 2, 1]
print(next_permutation(a))

a = [2, 3, 1]
print(next_permutation(a))

a = [1, 2, 3, 4, 6, 5]
print(next_permutation(a))
