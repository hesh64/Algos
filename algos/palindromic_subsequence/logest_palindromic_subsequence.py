"""
Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence, elements
read the same backward and forward.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing
the order of the remaining elements.


"""


def find_lps_length(st):
    return find_lps_rec(st, 0, len(st) - 1)


def find_lps_rec(st, start_index, end_index):
    if start_index > end_index:
        return 0

    if start_index == end_index:
        return 1

    if st[start_index] == st[end_index]:
        return 2 + find_lps_rec(st, start_index + 1, end_index - 1)

    c1 = find_lps_rec(st, start_index + 1, end_index)
    c2 = find_lps_rec(st, start_index, end_index - 1)

    return max(c1, c2)


def find_lps_lengthm(st):
    n = len(st)

    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_lps_recm(dp, st, 0, n - 1)


def find_lps_recm(dp, st, s, e):
    if s > e:
        return 0

    if s == e:
        return 1

    if dp[s][e] == -1:
        if st[s] == st[e]:
            dp[s][e] = 2 + find_lps_recm(dp, st, s + 1, e - 1)
            return dp[s][e]

        c1, c2 = find_lps_recm(dp, st, s + 1, e), find_lps_recm(dp, st, s, e - 1)
        dp[s][e] = max(c1, c2)
    return dp[s][e]


def find_lps_lengtht(st):
    n = len(st)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            if st[start] == st[end]:
                dp[start][end] = 2 + dp[start + 1][end - 1]
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
    return int(dp[0][n - 1])


"""
Given a string, find the minimum number of characters that we can remove to make it a palindrome.
"""


def minimum_deletions(st):
    n = len(st)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    # we start from the end to the front
    for start in range(n - 1, -1, -1):
        # from the start to the end
        for end in range(start + 1, n):
            if st[start] == st[end]:
                dp[start][end] = 2 + dp[start + 1][end - 1]
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

    # there is where all the difference is.
    return len(st) - dp[0][n - 1]


"""
Given a string, we want to cut it into pieces such that each piece is a palindrome. Write a function to return 
the minimum number of cuts needed."""


def is_palindrome(st, start, end):
    while start < end:
        if st[start] != st[end]:
            return False
        start += 1
        end -= 1

    return True


def palindrome_partition(st):
    return palindrome_partition_min(st, 0, len(st) - 1)


def palindrome_partition_min(st, start, end):
    # check if the full string is a palindrome -- then you need 0 cuts
    # start > end is our base case
    if start > end or is_palindrome(st, start, end):
        return 0

    # the max number of cuts we can make is  length - 1
    # basically chop every character into a standalone
    # string
    min_cuts = end - start
    for i in range(start, end + 1):
        # if st[start: i] is a palindrome, find that's 1 cut
        # how many more cuts for st[i: end]
        # also keeps comparing to find the minimum
        if is_palindrome(st, start, i):
            min_cuts = min(min_cuts, 1 + palindrome_partition_min(st, i + 1, end))

    return min_cuts


def main():
    print('brute')
    result = find_lps_length("abdbca")
    print(result)
    assert result == 5

    result = find_lps_length("cddpd")
    print(result)
    assert result == 3

    result = find_lps_length("pqr")
    print(result)
    assert result == 1

    print('\nmemo')
    result = find_lps_lengthm("abdbca")
    print(result)
    assert result == 5

    result = find_lps_lengthm("cddpd")
    print(result)
    assert result == 3

    result = find_lps_lengthm("pqr")
    print(result)
    assert result == 1

    print('\ntabul')
    result = find_lps_lengtht("abdbca")
    print(result)
    assert result == 5

    result = find_lps_lengtht("cddpd")
    print(result)
    assert result == 3

    result = find_lps_lengtht("pqr")
    print(result)
    assert result == 1

    print('\nminimum deletions')
    result = minimum_deletions("abdbca")
    print(result)
    result = minimum_deletions("cddpd")
    print(result)
    result = minimum_deletions("pqr")
    print(result)

    print('\nminimum palindrome cuts')
    st = 'abdbca'
    result = palindrome_partition_min(st, 0, len(st) - 1)
    print(result)


main()
