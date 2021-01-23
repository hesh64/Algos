"""
Words Concatenation (hard) #
Given a string and a list of words, find all the starting indices of substrings in
the given string that are a concatenation of all the given words exactly once
without any overlapping of words. It is given that all words are of the same length.
"""


def words_concatenation(string, words):
    indices = []
    char_freq = {}
    for word in words:
        for char in word:
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1

    start, match, word_length = 0, 0, len(words[0])
    max_length = word_length * len(words)

    for end in range(0, len(string)):
        if string[end] in char_freq:
            char_freq[string[end]] -= 1

            if char_freq[string[end]] == 0:
                match += 1

        if match == len(char_freq):
            indices.append(start)

        if end - start + 1 >= max_length:
            for i in range(word_length):
                prev = string[start]
                if prev in char_freq:
                    if char_freq[prev] == 0:
                        match -= 1
                    char_freq[prev] += 1
                start += 1

    return indices


def main():
    result = words_concatenation('catfoxcat', words=['cat', 'fox'])
    print(result)
    result = words_concatenation('catcatfoxfox', words=['cat', 'fox'])
    print(result)


main()
