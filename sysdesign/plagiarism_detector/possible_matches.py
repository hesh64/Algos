def possible_matches(plagiarised, students):
    words = {
        'none': []
    }
    for w in students:
        first_char = w[0]
        if first_char not in words:
            words[first_char] = []
        # w - word, 0 - first index
        words[first_char].append((w, 0))

    print(words)
    i = 0
    return possible_matches_helper(plagiarised, i, words)


# we are iterating over the string once, and we are
# iterating over every char in the tokens once
# so... Time O(S + SUM(token.length)) where S = len(string) and token is the word
# which if you convert this to graph terms O(V + E)
def possible_matches_helper(string, i, students):
    # if i >= len(string):
    #     return students['none']

    for i in range(len(string)):
        char = string[i]
        if char in students:
            # [(w, index), [w, index]]
            tokens = students[char]
            students[char] = []
            for (token, index) in tokens:
                while index + 1 < len(token) and token[index] == token[index + 1]:
                    index += 1
                # print(string[i])
                if token[index] == char and len(token) - 1 == index:
                    students['none'].append(token)
                elif token[index] == char:
                    new_index = index + 1
                    new_char = token[new_index]
                    if new_char not in students:
                        students[new_char] = []
                    students[new_char].append((token, new_index))
                else:
                    students[char].append((token, index))

    return students['none']


def main():
    students = ['a', 'bb', 'acd', 'ace']
    plagiarised = 'abcde'

    print(possible_matches(plagiarised, students))


main()
