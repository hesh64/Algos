mapping = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']


def compute(string, i, stack, perms):
    if i == len(string):
        perms.append(''.join(stack[:]))
        return

    chars = mapping[int(string[i]) - 2]
    for c in chars:
        stack.append(c)
        compute(string, i + 1, stack, perms)
        stack.pop()


def main():
    n = '2276696'
    i, stack, perms = 0, [], []
    compute(n, i, stack, perms)
    print(perms)


main()
