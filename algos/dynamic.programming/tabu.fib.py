# O(n) down from O(2^n)
# O(n)
def fib_tabu(n):
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(n):
        if i + 1 < n + 1:
            table[i + 1] += table[i]
        if i + 2 < n + 1:
            table[i + 2] += table[i]

    return table[n]


# O(n) down from O(2^n)
# O(1)
def fib_tabu_space_efficient(n):
    """wow"""
    last, second_last = 1, 0
    cur = 1
    for _ in range(2, n + 1):
        cur, second_last = last + second_last, last
        last = cur

    return cur


def main():
    n = 12
    result = fib_tabu(n)
    print('Fib(12):', result)
    n = 5
    result = fib_tabu(n)
    print(f'Fib({n}):', result)

    n = 12
    result = fib_tabu_space_efficient(n)
    print('Fib(12):', result)
    n = 5
    result = fib_tabu_space_efficient(n)
    print(f'Fib({n}):', result)


main()
