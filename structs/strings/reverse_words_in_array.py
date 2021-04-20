def reverse_words_in_sentence(string):
    n = len(string)
    s = n - 1
    result = ''
    while s >= 0:
        c = string[s]
        if c == ' ':
            if len(result) == 0 or result[-1] != c:
                result += c
        else:
            end = s
            while s > 0 and string[s - 1] != ' ':
                s -= 1

            result += string[s: end + 1]
        s -= 1
    result = result.rstrip()
    result = result.lstrip()
    return result


def reverse_words_in_char_array(chars):
    chars = list(chars)
    n = len(chars)
    s = n - 1
    h = -1
    while s >= 0:
        h = s
        while h > 0 and chars[s] != ' ' and chars[h - 1] != ' ':
            h -= 1

        if h < s:
            l, r = h, s
            while l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
            s = h
        s -= 1
    for i in range(len(chars) // 2):
        chars[i], chars[~i] = chars[~i], chars[i]
    return chars


def main():
    print(reverse_words_in_sentence('Alice Likes Bob'))
    print(reverse_words_in_sentence('Alice Likes Bob  '))
    print(reverse_words_in_sentence('Alice  Likes Bob  '))
    print(reverse_words_in_sentence(' Alice Likes Bob'))
    print(reverse_words_in_sentence(''))
    print(reverse_words_in_sentence('  '))
    print(reverse_words_in_sentence(' a'))
    print(reverse_words_in_sentence('b '))
    print(reverse_words_in_sentence(' c '))
    print(reverse_words_in_sentence("the sky is blue"))
    print(reverse_words_in_sentence("  hello world  "))
    print(reverse_words_in_sentence("a good   example"))
    print(reverse_words_in_sentence("  Bob    Loves  Alice   "))
    print(reverse_words_in_sentence("Alice does not even like bob"))
    print(reverse_words_in_sentence("EPY2giL"))
    print('\n\n')
    print(reverse_words_in_char_array('Alice Likes Bob'))
    print(reverse_words_in_char_array('Alice Likes Bob  '))
    print(reverse_words_in_char_array('Alice  Likes Bob  '))
    print(reverse_words_in_char_array(' Alice Likes Bob'))
    print(reverse_words_in_char_array(''))
    print(reverse_words_in_char_array('  '))
    print(reverse_words_in_char_array(' a'))
    print(reverse_words_in_char_array('b '))
    print(reverse_words_in_char_array(' c '))
    print(reverse_words_in_char_array("the sky is blue"))
    print(reverse_words_in_char_array("  hello world  "))
    print(reverse_words_in_char_array("a good   example"))
    print(reverse_words_in_char_array("  Bob    Loves  Alice   "))
    print(reverse_words_in_char_array("Alice does not even like bob"))
    print(reverse_words_in_char_array("EPY2giL"))


main()
