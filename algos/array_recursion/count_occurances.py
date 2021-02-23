def count(array, key):
    if len(array) == 0:
        return 0

    if array[0] == key:
        return 1 + count(array[1:], key)

    return count(array[1:], key)


"""Our task is to flip the elements of the array, meaning we will make the first
element of the array the last element, the second element the second last element, and so on.

"""


def invert(array):
    if len(array) == 0:
        return []

    if len(array) == 1:
        return array

    return invert(array[1:]) + array[:1]


def main():
    array = [1, 2, 1, 4, 5, 1]
    key = 1
    result = count(array, key)
    print(f'the digit {key} appears {result} times')

    print(invert(array))
    print(invert([1]))

main()
