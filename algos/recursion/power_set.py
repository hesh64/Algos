from collections import deque

s = sorted([1, 2, 3, 2])


def power_set(s, i, stack, sets):
    if i == len(s):
        sets.append(stack)
        return
    power_set(s, i + 1, stack, sets)
    power_set(s, i + 1, stack[:] + [s[i]], sets)


sets = []
power_set(s, 0, [], sets)

print(sets)


def power_sets(s):
    que = deque()
    que.append([])
    l = 0

    while l < len(s):
        size = len(que)
        for _ in range(size):
            k = que.popleft()
            que.append(k)
            if l > 0 and s[l] == s[l - 1]:
                continue
            que.append(k + s[l: l + 1])

        l += 1

    return list(que)


print(sorted(power_sets(s), key=lambda array: len(array)))

n, k, s, u, r = 5, 2, [], set(), []


def whatever(n, k, s, u, r):
    if k == 0:
        r.append(s[:])
        return

    for i in range(1, n + 1):
        if len(s) > 0 and s[-1] >= i:
            continue

        s.append(i)
        whatever(n, k - 1, s, set(), r)
        s.pop()

    return r


print(whatever(n, k, s, u, r))
