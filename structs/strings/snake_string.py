def snake_string(s):
    chars = {0: [], 1: [], -1: []}
    start, direction = 0, 1

    for c in s:
        if start == 0:
            chars[start].append(c)
            start += 1 if direction == 1 else -1
        else:
            direction = -1 if start == 1 else 1
            chars[start].append(c)
            start += -1 if start == 1 else 1

    return ''.join(chars[1] + chars[0] + chars[-1])


def main():
    print(snake_string('Hello World!'))


main()
