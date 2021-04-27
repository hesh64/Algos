from functools import lru_cache

tri = [
    [2],
    [4, 4],
    [8, 5, 6],
    [4, 2, 6, 2],
    [1, 5, 2, 3, 4],
    [1, 5, 2, 3, 4, 7]
]


def weighted_path(tri):
    c = 0

    @lru_cache(None)
    def helper(h, i):
        nonlocal tri, c
        c += 1
        if len(tri) <= h or len(tri[h]) <= i:
            return 0

        right = helper(h + 1, i + 1)
        left = helper(h + 1, i)

        return tri[h][i] + min(left, right)

    r = helper(0, 0)
    print(c)
    return r


print(weighted_path(tri))
