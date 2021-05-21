def find_all_sums_to_100(input):
    if len(input) == 0:
        return 0
    combo = []

    def helper(start, end, total, stack):
        if start == end and total == 100:
            combo.append(''.join(stack))
            return True

        if start == end:
            return False

        for k in range(1, end):
            if start + k > end:
                break

            num = int(input[start: start + k])

            stack.append(str(-num))
            helper(start + k, end, -num + total, stack)
            stack.pop()

            stack.append('+' + str(num) if len(stack) else str(num))
            helper(start + k, end, num + total, stack)
            stack.pop()

        return combo

    return helper(0, len(input), 0, [])


for i, w in enumerate(find_all_sums_to_100('123456789')):
    print(i + 1, w)
