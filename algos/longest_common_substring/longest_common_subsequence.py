"""
Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing
the order of the remaining elements.
"""


def find_lcs_len(st1, st2):
    n1, n2 = len(st1), len(st2)

    if n1 == 0 or n2 == 0:
        return 0
    return find_lcs(st1, st2, 0, 0)


def find_lcs(st1, st2, i1, i2):
    if len(st1) == i1 or len(st2) == i2:
        return 0
    if st1[i1] == st2[i2]:
        return 1 + find_lcs(st1, st2, i1 + 1, i2 + 1)

    c1 = find_lcs(st1, st2, i1 + 1, i2)
    c2 = find_lcs(st1, st2, i1, i2 + 1)
    return max(c1, c2)


def find_lcs_len_m(st1, st2):
    n1, n2 = len(st1), len(st2)
    if n1 == 0 or n2 == 0:
        return 0
    dp = [[-1 for _ in range(n2)] for _ in range(n1)]
    return find_lcs_m(dp, st1, st2, 0, 0)


def find_lcs_m(dp, st1, st2, i1, i2):
    if len(st1) == i1 or len(st2) == i2:
        return 0

    if dp[i1][i2] == -1:
        if st1[i1] == st2[i2]:
            dp[i1][i2] = 1 + find_lcs_m(dp, st1, st2, i1 + 1, i2 + 1)
            return dp[i1][i2]

        c1 = find_lcs_m(dp, st1, st2, i1 + 1, i2)
        c2 = find_lcs_m(dp, st1, st2, i1, i2 + 1)

        dp[i1][i2] = max(c1, c2)
    return dp[i1][i2]


def main():
    print('brute force')
    print(find_lcs_len("abdca", "cbda"))
    print(find_lcs_len("passport", "ppsspt"))

    print('\nmemo')
    print(find_lcs_len_m("abdca", "cbda"))
    print(find_lcs_len_m("passport", "ppsspt"))


main()
