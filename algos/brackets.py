def match_brackets(brackets):
    stack = []
    open = ['[', '(', '{']
    close = {']': '[', ')': '(', '}': '{'}

    for c in brackets:
        if c in open:
            stack.append(c)

        elif c in close:
            open_bracket = close[c]
            if len(stack) and open_bracket == stack[-1]:
                stack.pop(-1)
            else:
                return False

    if len(stack):
        return False

    return True


print(match_brackets('{]}'))
