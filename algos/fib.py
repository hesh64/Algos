# time O(2 ^ n)
# space O(n)
def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5

# print(fib(100))  # takes for ever

print('memo')


# Time O(n)
# Space O(n ^ 2)
def fib_mem(n, memo=dict()):
    if n in memo:
        return memo[n]

    if n == 1 or n == 2:
        return 1

    memo[n] = fib_mem(n - 1, memo) + fib_mem(n - 2, memo)
    return memo[n]


print(fib_mem(300))  # fast


# time O(n)
# space O(n)
def fib_tab(n):
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(len(table)):
        if i + 1 < len(table):
            table[i + 1] += table[i]

        if i + 2 < len(table):
            table[i + 2] += table[i]

    return table[n]


print(fib_tab(1))
print(fib_tab(3))
print(fib_tab(4))
print(fib_tab(5))
print(fib_tab(300))
