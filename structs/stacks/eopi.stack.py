def evaluate_rpn(string):
    chars = [int(c) if c.isnumeric() else c for c in reversed(string.split(','))]

    while len(chars) > 1:
        l, r, op = chars.pop(), chars.pop(), chars.pop()

        if op == '+':
            chars.append(l + r)
        elif op == '-':
            chars.append(l - r)
        elif op == '*':
            chars.append(l * r)
        elif op == '/':
            chars.append(l / r)

    return chars[-1]


def well_formed_string(string):
    left = {'{': '}', '[': ']', '(': ')'}
    right = {'}': '{', ']': '[', ')': '('}

    s = []
    for i in range(len(string) - 1, -1, -1):
        char = string[i]
        if char in right:
            s.append(char)
        elif char in left:
            if s[-1] == left[char]:
                s.pop()
            else:
                return False

    return len(s) == 0


def who_can_see_the_sunset(buildings):
    max_b = -float('inf')

    def cal(bi):
        nonlocal max_b
        if bi > max_b:
            max_b = bi
            return True
        return False

    return list(map(cal, buildings))


def main():
    print(evaluate_rpn('3,4,+,2,*,1,+'))
    print(well_formed_string('[(){}()]{[]}'))
    print(well_formed_string('[(){}()]{[}'))
    print(who_can_see_the_sunset([1, 2, 3, 4, 5, 2, 3, 7]))


main()
