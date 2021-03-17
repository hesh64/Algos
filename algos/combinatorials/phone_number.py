"""
Given a phone number that contains digits from 2–9, find all possible
letter combinations the phone number could translate to.
"""

numbers = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def letter_combinations(digits):
    def dfs(input, index, perms, total):
        if len(perms) == len(input):
            total.append(''.join(perms))
            return

        for c in numbers[input[index]]:
            perms.append(c)
            dfs(input, index + 1, perms, total)
            perms.pop()

    total = []
    dig = [d for d in digits]
    dfs(dig, 0, [], total)
    return total


print(letter_combinations('56'))
print(letter_combinations('23'))
print(letter_combinations('235'))
