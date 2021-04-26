"""
Remove Tabs in a String
Our task is to remove all tabs from a string. This includes the character \t and " " from a string.

"""


def remove(string):
    if not string:
        return ''

    if string[0] == '\t' or string[0] == ' ':
        return remove(string[1:])
    else:
        return string[0] + remove(string[1:])


"""This means that we will remove all extra instances of a character when multiple instances are 
found together. In other words, only one instance should remain after this process.
"""


def remove_adjacent_duplicates(string):
    if not string:
        return ''

    elif len(string) == 1:
        return string

    if string[0] == string[1]:
        return remove_adjacent_duplicates(string[1:])

    return string[0] + remove_adjacent_duplicates(string[1:])


"""
Lexicographical means that something is organized according to alphabetical order.

Lexicographical means that something is organized according to alphabetical order.

Lower case letters are different from upper case letters and are therefore treated as different
elements. All upper case letters come before lower case letters. Alphabetic sorting is as
follows: $A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a,
b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z$

"""


def merge(string1, string2):
    if string1 == '':
        if string2 == '':
            return ''
        return string2

    elif string2 == '':
        return string1

    elif string1[0] > string2[0]:
        return string2[0] + merge(string1, string2[1:])

    return string1[0] + merge(string1[1:], string2)


"""Implement a function that takes a string testVariable and returns the length of the string."""


def string_len(string):
    if string == '':
        return 0

    return 1 + string_len(string[1:])


"""Implement a function that takes a variable testVariable, which contains a string of
 digits, and prints the sum of those digits.
"""


def sum_digits(string):
    if string == '':
        return 0

    return int(string[0]) + sum_digits(string[1:])


"""
Write a function that takes a variable testVariable, which contains a string,
and checks whether or not it is a palindrome.

"""


def is_palindrome(string):
    # all 0-1 chars are palindromes
    if len(string) <= 1:
        return True

    return string[0] == string[-1] and is_palindrome(string[1:-1])


def main():
    result = remove('hello world')
    print(result)

    result = remove_adjacent_duplicates('hellowwwrd')
    print(result)

    string1, string2 = 'ACEGT', 'BDFL'
    result = merge(string1, string2)
    print(f'Merging 2 lists: {result}')

    length_of_string = string_len(string1)
    print(f'length of string {string1} is {length_of_string}')

    sum_of_digits = sum_digits('345')
    print(f'sum of "345" is {sum_of_digits}')

    pal = 'madam'
    result = is_palindrome(pal)
    print(f'is {pal} a palindrome? {result}')


main()
