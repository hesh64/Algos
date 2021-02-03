"""
Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
find the length of the longest substring having the same letters after replacement.

"""


def string_replacement_k(string, k):
    seen = {}
    start, max_len, max_repeat = 0, 0, 0

    for end in range(len(string)):
        if string[end] not in seen:
            seen[string[end]] = 0
        seen[string[end]] += 1

        # max_repeat is the majority repeating letter
        max_repeat = max(max_repeat, seen[string[end]])

        # here we wanna know if end - start + 1 - majority repeating letter leaves enough
        # letters to exchange -- we exchange k letters
        # if we have too many letters to exchange then move up start by one
        # adjust the counts
        if end - start + 1 - max_repeat > k:
            seen[string[start]] -= 1
            start += 1

        # this is how much distance we can go with k exchanges letters
        max_len = max(max_len, end - start + 1)
    return max_len


def main():
    string, k = "aabccbb", 2
    result = string_replacement_k(string, k)
    print(result)
    string, k = "abbcb", 1
    result = string_replacement_k(string, k)
    print(result)


main()
