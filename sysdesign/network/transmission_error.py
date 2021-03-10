# O(n) time O(1) space
def transmission_error(stack):
    i, j = 0, len(stack) - 1
    once = 1
    while i < j:
        if stack[i] != stack[j] and once > 0:
            once -= 1
            j -= 1
        elif once == 0:
            return False
        i += 1
        j -= 1
    return True


def main():
    # so in this scenario we know that the only half
    # where an error can happen is in the return route.
    # where there will be an additional value
    stack = [1, 2, 4, 3, 3, 4, 2, 1]
    print(transmission_error(stack))

    stack = [1, 2, 3, 3, 4, 2, 1]
    print(transmission_error(stack))

    stack = [1, 2, 3, 3, 4, 2, 10]
    print(transmission_error(stack))


main()
