"""
A girl lost the key to her locker (note: The key is only numeric).
She remembers the number of digits N as well as the sum S of all the
digits of her password. She also knows that her password is the largest number
of N digits that can be possible with a given sum S.

Implement a function that would help her retrieve her key.
"""


def find_largest_number(number_of_digits, sum_of_digits):
    """
    Finds the largest number with given number of digits and sum of Digits
    :param number_of_digits: Number of digits
    :param sum_of_digits: Sum of digits
    :return: Possible largest number
    """

    # The only reason this works is because we KNOW
    # that the digits [...] sum up to sum_of_digits
    # so they must fit exactly

    array = [0] * number_of_digits
    mul = sum_of_digits // 9
    remainder = sum_of_digits % 9
    for i in range(mul):
        array[i] = 9
    array[mul] = remainder

    return array


if __name__ == '__main__':
    print(find_largest_number(3, 20))
    print(find_largest_number(4, 20))
    print(find_largest_number(5, 19))
    print(find_largest_number(1, 0))
    print(find_largest_number(10, 0))
    print(find_largest_number(10, 1))
