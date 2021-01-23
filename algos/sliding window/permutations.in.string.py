"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example,
“abc” has the following six permutations:

"""


def permutation_in_a_string(string, pattern):
    p = {}
    for end in range(len(string)):
        if string[end] in pattern:
            if string[end] not in p:
                p[string[end]] = 0
            p[string[end]] += 1
        else:
            p = {}

        if sum(p.values()) == len(pattern):
            return True

    return False


# so we had to go through the pattern and create a char freq dict
# that's O(k) where pattern.length = k
# we have to iterate through the object, nad processed each character at the
# most twice so thats O(n+n)
# O(2n+k) -> O(n+k)
def course_solution(string, pattern):
    start, matched = 0, 0

    char_freq = {}
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    for end in range(len(string)):
        if string[end] in char_freq:
            char_freq[string[end]] -= 1

            if char_freq[string[end]] == 0:
                matched += 1

        # x many occurances of say 'o' would yield 1 match
        # this relation is not linear between characters
        # and match amount
        if matched == len(char_freq):
            return True

        if end >= len(pattern) - 1:
            last = string[start]
            # this is what we are here for
            # we just need to increment the start to decrease the window,
            # but there is follow up work which depends on the previous
            # position start was at
            start += 1

            if last in char_freq:
                if char_freq[last] == 0:
                    matched -= 1
                char_freq[last] += 1

    return False


# String Anagrams (hard) #
# Given a string and a pattern, find all anagrams of the pattern in the given string.
#
# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
#
# this is O(n) + k check per step of n
# so O(n * k)
def string_anagram(string, pattern):
    start = 0
    found = []

    for end in range(len(string)):
        if end - start + 1 >= len(pattern):
            count = 0
            for char in pattern:
                if char in string[start: end + 1]:
                    count += 1

            if count == len(pattern):
                found.append(start)
            start += 1

    return found


# we an actually address this with the same base solution of the sliding window
def string_anagram_correct(string, pattern):
    start, matched = 0, 0
    char_freq = {}
    anagrams = []

    for p in pattern:
        if p not in char_freq:
            char_freq[p] = 0
        char_freq[p] += 1

    for end in range(len(string)):
        if string[end] in char_freq:
            char_freq[string[end]] -= 1
            if char_freq[string[end]] == 0:
                matched += 1

        if matched == len(pattern):
            anagrams.append(start)

        if end >= len(pattern) - 1:
            prev = string[start]
            if prev in char_freq:
                if char_freq[prev] == 0:
                    matched -= 1
                char_freq[prev] += 1
                start += 1

    return anagrams


"""
Smallest Window containing Substring (hard) #
Given a string and a pattern, find the smallest substring 
in the given string which has all the characters of the given pattern.
"""


# there is a better way!
def smallest_substring(string, pattern):
    for k in range(len(pattern), len(string)):
        char_freq = {}
        for char in pattern:
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1

        start, matched = 0, 0

        for end in range(len(string)):
            if string[end] in char_freq:
                char_freq[string[end]] -= 1
                if char_freq[string[end]] == 0:
                    matched += 1

            if end >= k:
                prev = string[start]
                start += 1

                if prev in char_freq:
                    if char_freq[prev] == 0:
                        matched -= 1
                    char_freq[prev] += 1

            if matched == len(char_freq):
                return string[start:end + 1]

    return '""'


def smallest_substring_better(string, pattern):
    char_freq = {}
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    start, matched = 0, 0
    shortest_match = string

    for end in range(len(string)):
        if string[end] in char_freq:
            char_freq[string[end]] -= 1
            if char_freq[string[end]] == 0:
                matched += 1

        if matched == len(char_freq):
            while True:
                prev = string[start]
                if prev in char_freq:
                    if char_freq[prev] == 0:
                        break
                    char_freq[prev] += 1
                start += 1

            if len(string[start:end + 1]) < len(shortest_match):
                shortest_match = string[start:end + 1]

    return shortest_match if len(shortest_match) != len(string) else ''


# O(n + k)
def smallest_substring_adjusted(string, pattern):
    char_freq = {}
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    start, matched = 0, 0
    shortest_match = string

    for end in range(len(string)):
        if string[end] in char_freq:
            char_freq[string[end]] -= 1
            if char_freq[string[end]] == 0:
                matched += 1

        while matched == len(char_freq):
            if len(string[start:end + 1]) < len(shortest_match):
                shortest_match = string[start:end + 1]

            prev = string[start]
            if prev in char_freq:
                if char_freq[prev] == 0:
                    matched -= 1
                char_freq[prev] += 1
            start += 1

    return shortest_match if len(shortest_match) != len(string) else ''


def main():
    result = permutation_in_a_string(string="oidbcaf", pattern="abc")
    print(result)
    result = permutation_in_a_string(string="odicf", pattern="dc")
    print(result)
    result = permutation_in_a_string(string="bcdxabcdy", pattern="bcdyabcdx")
    print(result)
    result = permutation_in_a_string(string="aaacb", pattern="abc")
    print(result)

    print('\ncourse_solution:')
    result = course_solution(string="oidbcaf", pattern="abc")
    print(result)
    result = course_solution(string="odicf", pattern="dc")
    print(result)
    result = course_solution(string="bcdxabcdy", pattern="bcdyabcdx")
    print(result)
    result = course_solution(string="aaacb", pattern="abc")
    print(result)

    print('\n\nanagrams')
    result = string_anagram(string="abbcabc", pattern="abc")
    print(result)

    print('\n\nanagrams')
    result = string_anagram_correct(string="abbcabc", pattern="abc")
    print(result)

    print('\nsmallest window containing substring')
    result = smallest_substring("aabdec", pattern="abc")
    print(result)
    print('\nsmallest window containing substring')
    result = smallest_substring("abdbca", pattern="abc")
    print(result)
    print('\nsmallest window containing substring')
    result = smallest_substring("adcad", pattern="abc")
    print(result)

    print('\nlinear smallest window containing substring\n')
    result = smallest_substring_better("aabdec", pattern="abc")
    print(result)
    print('\nsmallest window containing substring\n')
    result = smallest_substring_better("abdbca", pattern="abc")
    print(result)
    print('\nsmallest window containing substring\n')
    result = smallest_substring_better("adcad", pattern="abc")
    print(result)


    print('\nlinear adjusted smallest window containing substring\n')
    result = smallest_substring_adjusted("aabdec", pattern="abc")
    print(result)
    print('\nsmallest window containing substring\n')
    result = smallest_substring_adjusted("abdbca", pattern="abc")
    print(result)
    print('\nsmallest window containing substring\n')
    result = smallest_substring_adjusted("adcad", pattern="abc")
    print(result)


main()
