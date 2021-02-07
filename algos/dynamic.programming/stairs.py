"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a
function to count the number of possible ways that the child can run up the stairs.

"""


def hop_rec(n, memo={}):
    # good base case
    if n == 0:
        return 1

    # bad base case
    if n < 0:
        return 0

    if n in memo:
        print('we hit this case')
        return memo[n]

    memo[n] = sum([hop_rec(n - num_of_hops, memo) for num_of_hops in [1, 2, 3] if n >= num_of_hops])
    return memo[n]


def hop_tab(n):
    lookup_table = [0 for x in range(n + 1)]
    # setting the first three values
    lookup_table[0] = 1
    lookup_table[1] = 1
    lookup_table[2] = 2

    for i in range(3, n + 1):
        lookup_table[i] = lookup_table[i - 1] + lookup_table[i - 2] + lookup_table[i - 3]

    return lookup_table[n]


def hop_tab_space(n):
    if n < 0:
        return 0
    if n <= 2:
        return n

    third, second, last = 1, 1, 2
    cur = 0

    for _ in range(3, n + 1):
        cur = last + second + third
        third, second, last = second, last, cur
        
    return cur


def hop(n):
    return hop_rec(n)


print(hop_rec(400))
print(hop_tab(4000))
print(hop_tab_space(4000))
