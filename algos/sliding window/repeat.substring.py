# O(n)
# space is max 26 O(k) where k <= 26 english alphabet
def longest_repeat(string):
    max_length = 0
    start = 0
    chars = {}

    for end in range(len(string)):
        if string[end] not in chars:
            chars[string[end]] = 0

        chars[string[end]] += 1

        if chars[string[end]] > 1:
            max_length = max(end - start, max_length)
            start = end
            chars = {string[end]: 1}
    return max_length


'''
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’
letters with any letter, find the length of the longest substring having the same letters after
replacement.
'''


# todo come back to this.
def max_length_replace_k(string, k):
    start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    for end in range(len(string)):
        if string[end] not in frequency_map:
            frequency_map[string[end]] = 0
        frequency_map[string[end]] += 1

        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[string[end]])

        if (end - start + 1 - max_repeat_letter_count) > k:
            frequency_map[string[string]] -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


'''
Given an array containing 0s and 1s, if you are allowed 
to replace no more than ‘k’ 0s with 1s, find the length of 
the longest contiguous subarray having all 1s.
'''


# O(n + n) -> O(n)
def longest_zeros_and_ones(array, k):
    start = 0
    max_1s = 0
    zeros = 0

    for end in range(len(array)):
        if array[end] == 0:
            zeros += 1

        while zeros > k:
            if array[start] == 0:
                zeros -= 1
            start += 1

        max_1s = max(end - start + 1, max_1s)

    return max_1s


def main():
    result = longest_repeat('aabccbb')
    print('longest_repeat', result)

    result = longest_repeat('abbb')
    print('longest_repeat', result)

    result = longest_repeat('abccde')
    print('longest_repeat', result)

    # this works wow...
    result = longest_zeros_and_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2)
    print(result)

    result = longest_zeros_and_ones([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3)
    print(result)


main()
