def search(string, pattern):
    p = len(pattern)
    i = 0
    for end in range(0, len(string)):
        if string[end] == pattern[i]:
            i += 1
            if i == p:
                return end - i + 1
        else:
            i = 0

    return -1


def main():
    res = search('lalopalalali', 'lala')
    print(res)


main()
