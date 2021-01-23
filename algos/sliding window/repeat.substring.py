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


def main():
    result = longest_repeat('aabccbb')
    print('longest_repeat', result)

    result = longest_repeat('abbb')
    print('longest_repeat', result)

    result = longest_repeat('abccde')
    print('longest_repeat', result)


main()
