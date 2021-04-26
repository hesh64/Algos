from collections import deque


def match_bracket(string):
    q = deque()
    brackets = {']': '[', ')': '(', '}': '{'}

    for char in string:
        if char in ['[', '{', '(']:
            q.append(char)
        elif char in [']', '}', ')']:
            if len(q) and brackets[char] == q[-1]:
                q.pop()
            else:
                return False

    return len(q) == 0


def main():
    string = '[]{}()'
    result = match_bracket(string)
    print(f'{string}', result)

    string = '()'
    result = match_bracket(string)
    print(f'{string}', result)

    string = '('
    result = match_bracket(string)
    print(f'{string}', result)

    string = ']'
    result = match_bracket(string)
    print(f'{string}', result)


main()
