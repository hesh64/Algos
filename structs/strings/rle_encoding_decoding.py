def encode(s):
    if len(s) == 0:
        return ''

    letter, count = None, None
    rec = []
    for end in range(len(s)):
        if letter is None:
            letter = s[end]
            count = 1
        else:
            if s[end] == letter:
                count += 1
            else:
                rec.extend([str(count), letter])
                letter = s[end]
                count = 1
    rec.extend([str(count), letter])
    
    return ''.join(rec)


def decode(s):
    if len(s) == 0:
        return ''

    result = []
    for i in range(0, len(s), 2):
        count = s[i]
        letter = s[i + 1]
        result.append(letter * int(count))

    return ''.join(result)


def main():
    r = encode('aaaabcccaa')
    print(r)
    d = decode(r)
    print(d)


main()
