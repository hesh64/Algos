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


main()
