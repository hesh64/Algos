def longest_substring_w_k_distinct(string, k):
    longest = -1
    for end in range(len(string)):
        for start in range(0, end):
            # this is an expensive operation
            # string to list to set -> let's try to fix taht
            if len(set(list(string[start:end]))) == k:
                longest = max(longest, len(string[start:end]))

    return longest


# O(n+n) -> O(n)
def longest_substring_w_k_distinct2(string, k):
    chars = {}
    longest = -1
    start = 0
    for end in range(len(string)):
        if string[end] not in chars:
            chars[string[end]] = 0

        chars[string[end]] += 1

        while len(chars) > k:
            chars[string[start]] -= 1
            if chars[string[start]] == 0:
                del chars[string[start]]

            start += 1

        longest = max(longest, end - start + 1)

    return longest


def main():
    result = longest_substring_w_k_distinct('araaci', k=2)
    print('Longest substring with k distinct chars is:', result)

    result = longest_substring_w_k_distinct('araaci', k=1)
    print('Longest substring with k distinct chars is:', result)

    result = longest_substring_w_k_distinct('cbbebi', k=3)
    print('Longest substring with k distinct chars is:', result)

    result = longest_substring_w_k_distinct2('araaci', k=2)
    print('Longest substring with k distinct chars 2 is:', result)

    result = longest_substring_w_k_distinct2('araaci', k=1)
    print('Longest substring with k distinct chars 2 is:', result)

    result = longest_substring_w_k_distinct2('cbbebi', k=3)
    print('Longest substring with k distinct chars 2 is:', result)


main()
