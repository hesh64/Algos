def fact(n):
    if n == 1:
        return 1

    return n * fact(n - 1)


print(fact(1))
print(fact(2))
print(fact(3))
print(fact(5))

# Time: O(n)
# Space: O(n)
