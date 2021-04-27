from functools import lru_cache


def grid_walk(n, m):
    @lru_cache(None)
    def helper(x, y):
        if x == y == 0:
            return 1

        ways_top = x if x == 0 else helper(x - 1, y)
        ways_left = y if y == 0 else helper(x, y - 1)
        return ways_top + ways_left

    return helper(n - 1, m - 1)


def grid_walk2(size, i, j):
    x, y = size[0] - i, size[1] - j

    if x == 0 or y == 0:
        return 0

    if x == 1 and y == 1:
        return 1

    return grid_walk2(size, i + 1, j) + grid_walk2(size, i, j + 1)


print(grid_walk(5, 5))
print(grid_walk2((5, 5), 0, 0))
