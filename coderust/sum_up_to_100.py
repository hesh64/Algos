def find_all_sums_to_100(input):
    if len(input) == 0:
        return 0
    combo = []

    def helper(start, end, total, string):
        if start == end and total == 100:
            combo.append(string)
            return True

        if start == end:
            return False

        for k in range(1, end):
            if start + k > end:
                break

            num = int(input[start: start + k])
            helper(start + k, end, -num + total, string + str(-num))
            helper(start + k, end, num + total, string + '+' + str(num) if len(string) else str(num))

        return combo

    return helper(0, len(input), 0, '')


for w in find_all_sums_to_100('123456789'):
    print(w)
