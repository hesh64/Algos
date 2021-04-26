def backspace_compare_old(str1, str2):
    def process(string):
        lst = list(string)
        p1 = 0

        for p2 in range(len(lst)):
            if lst[p2] == '#':
                p1 = max(0, p1 - 1)

            else:
                lst[p1] = lst[p2]
                p1 += 1

        return ''.join(lst[: p1])

    s1 = process(str1)
    s2 = process(str2)
    # print(s1, s2)
    return s1 == s2


def backspace_compare(str1, str2):
    i, i_ignore = len(str1) - 1, 0
    j, j_ignore = len(str2) - 1, 0

    while i >= 0 and j >= 0:
        if str1[i] == '#':
            i_ignore += 1
            i -= 1
            continue

        if str2[j] == '#':
            j_ignore += 1
            j -= 1
            continue

        if i_ignore > 0 or j_ignore > 0:
            if i_ignore > 0:
                i_ignore -= 1
                i -= 1
                continue

            if j_ignore > 0:
                j_ignore -= 1
                j -= 1
                continue

        if i >= 0 and j >= 0 and str1[i] == str2[j]:
            i -= 1
            j -= 1
        else:
            return False

    # print(i, j)
    return True


def main():
    print(backspace_compare('xy#z', 'xzz#'))
    print(backspace_compare('xy#z', 'xyz#'))
    print(backspace_compare('xp#', 'xyz##'))
    print(backspace_compare('xywrrmp', 'xywrrmu#p'))
    print(backspace_compare("y#fo##f", "y#f#o##f"))
    # print(backspace_compare("bxj##tw", "bxj###tw"))

    print('--->')
    print(backspace_compare_old('xy#z', 'xzz#'))
    print(backspace_compare_old('xy#z', 'xyz#'))
    print(backspace_compare_old('xp#', 'xyz##'))
    print(backspace_compare_old('xywrrmp', 'xywrrmu#p'))
    print(backspace_compare_old("y#fo##f", "y#f#o##f"))
    # print(backspace_compare_old("bxj##tw", "bxj###tw"))


main()
