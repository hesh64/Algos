def fib(n):
    """
    classic fib
    :param n:
    :return:
    """
    if n in [0, 1]:
        return n

    return fib(n - 1) + fib(n - 2)


# say this is our max array size
fib_cache = [None] * 10000


def fib_c(n):
    if fib_cache[n] is None:
        fib_cache[n] = fib_c(n - 1) + fib_c(n - 2)

    return fib_cache[n]


def fib_c_driver(n):
    fib_cache[0] = 0
    fib_cache[1] = 1
    for i in range(2, len(fib_cache)):
        fib_cache[i] = None

    return fib_c(n)


print(fib_c_driver(8))


def fib_t(n):
    if n < 2:
        return n
    f2, f1, next = 0, 1, 1
    for i in range(2, n + 1):
        next = f2 + f1
        f1, f2 = next, f1

    return next


print(fib_t(8))
