"""
Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which is common in both the strings.

"""


# O(3 ^(m + n)) where m len(s1) n = len(s2)
def find_lcs_length(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0

    return find_lcs(s1, s2, 0, 0, 0)


def find_lcs(s1, s2, i1, i2, c):
    if len(s1) == i1 or len(s2) == i2:
        return c

    if s1[i1] == s2[i2]:
        c = find_lcs(s1, s2, i1 + 1, i2 + 1, c + 1)

    c1 = find_lcs(s1, s2, i1 + 1, i2, 0)
    c2 = find_lcs(s1, s2, i1, i2 + 1, 0)

    return max(c, c1, c2)


# O(Dude who can know ^ (n! + help))
def find_lcs_length_m(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0

    n1 = len(s1)
    n2 = len(s2)
    max_len = min(n1, n2)
    dp = [[[-1 for _ in range(max_len)] for _ in range(len(s2))] for _ in range(len(s1))]
    return find_lcs_m(dp, s1, s2, 0, 0, 0)


def find_lcs_m(dp, s1, s2, i1, i2, c):
    if len(s1) == i1 or len(s2) == i2:
        return c

    if dp[i1][i2][c] == -1:
        c1 = c
        if s1[i1] == s2[i2]:
            c1 = find_lcs_m(dp, s1, s2, i1 + 1, i2 + 1, c + 1)
        c2 = find_lcs_m(dp, s1, s2, i1 + 1, i2, 0)
        c3 = find_lcs_m(dp, s1, s2, i1, i2 + 1, 0)

        dp[i1][i2][c] = max(c1, c2, c3)
    return dp[i1][i2][c]


# O(m * n)
def find_lcs_tabul(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1 == 0 or n2 == 0:
        return 0

    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    max_len = 0
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            max_len = max(max_len, dp[i][j])

    return max_len


def main():
    print('brute force')
    s1, s2 = 'abdca', 'cbda'
    result = find_lcs_length(s1, s2)
    print(result)

    s1, s2 = "passport", "ppsspt"
    result = find_lcs_length(s1, s2)
    print(result)

    print('\nmemo')
    s1, s2 = 'abdca', 'cbda'
    result = find_lcs_length_m(s1, s2)
    print(result)

    s1, s2 = "passport", "ppsspt"
    result = find_lcs_length_m(s1, s2)
    print(result)

    print('\ntabul')
    s1, s2 = 'abdca', 'cbda'
    result = find_lcs_tabul(s1, s2)
    print(result)

    s1, s2 = "passport", "ppsspt"
    result = find_lcs_tabul(s1, s2)
    print(result)


main()
