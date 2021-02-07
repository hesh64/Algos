# O(n) down from O(2^n)
# O(n)
def fib_memo(n, memo={}):
    if n <= 2:
        return 1

    if n - 1 not in memo:
        memo[n - 1] = fib_memo(n - 1, memo)

    if n - 2 not in memo:
        memo[n - 2] = fib_memo(n - 2, memo)

    return memo[n - 1] + memo[n - 2]


def main():
    n = 12
    result = fib_memo(n)
    print('Fib(12):', result)
    n = 5
    result = fib_memo(n)
    print(f'Fib({n}):', result)


main()
