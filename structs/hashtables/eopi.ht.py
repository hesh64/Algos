def check_if_string_is_plandromic(string):
    chars = {}
    for c in string:
        if c not in chars:
            chars[c] = 0
        chars[c] += 1

    odd = False
    for k in chars:
        if chars[k] % 2:
            if odd is False:
                odd = True
            else:
                return False

    return True


def main():
    print(check_if_string_is_plandromic('edified'))


main()
