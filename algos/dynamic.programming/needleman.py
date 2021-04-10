def needle(str1, str2):
    m = len(str1)
    n = len(str2)

    a = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        a[i][0] = i

    for j in range(n + 1):
        a[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            a[i][j] = min(a[i - 1][j - 1] + int(str1[i - 1] != str2[j - 1]), a[i - 1][j] + 1, a[i][j - 1] + 1)

    return a[m][n]


if __name__ == '__main__':
    str1, str2 = 'AGGGCT', 'AGGCA'
    print(needle(str1, str2))

    str1, str2 = 'AGTACG', 'ACATAG'
    print(needle(str1, str2))

    str1, str2 = 'salin1', 'salim1'
    print(needle(str1, str2))
