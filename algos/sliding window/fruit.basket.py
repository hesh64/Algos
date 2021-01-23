# O(n + n) -> O(n)
def fruit_into_two_baskets(array):
    chars = {}
    start = 0
    max_length = 0

    # this goes through the array once
    for end in range(len(array)):
        if array[end] not in chars:
            chars[array[end]] = 0

        chars[array[end]] += 1

        # at the most this will process each char once
        while len(chars) > 2:
            chars[array[start]] -= 1
            if chars[array[start]] == 0:
                del chars[array[start]]

            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


def main():
    result = fruit_into_two_baskets(['A', 'B', 'C', 'A', 'C'])
    print(result)

    result = fruit_into_two_baskets(['A', 'B', 'C', 'B', 'C', 'B'])
    print(result)

    result = fruit_into_two_baskets(['A', 'B', 'C', 'B', 'B', 'C'])
    print(result)


main()
