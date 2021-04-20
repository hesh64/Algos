def section_ip_address(s):
    def is_valid(s):
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)

    results, parts = [], [''] * 4
    for i in range(1, min(len(s), 4)):
        parts[0] = s[:i]
        if is_valid(parts[0]):
            for j in range(1, min(len(s) - i, 4)):
                parts[1] = s[i: i + j]
                if is_valid(parts[1]):
                    for k in range(1, min(len(s) - i - j, 4)):
                        parts[2] = s[i + j: i + j + k]
                        parts[3] = s[i + j + k:]
                        if is_valid(parts[2]) and is_valid(parts[3]):
                            results.append('.'.join(parts))

    return results


def main():
    ips = section_ip_address('19216811')
    for o in ips:
        print(o)


# section('19216811')


main()
