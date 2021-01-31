"""
In a non-empty array of integers, every number appears twice except for one, find that single number.
"""


def single_number(nums):
    xor = 0

    for num in nums:
        xor ^= num

    return xor


"""
Every non-negative integer N has a binary representation, for example, 8 can be represented as “1000” in binary and 7
as “0111” in binary.

The complement of a binary representation is the number in binary that we get when we change every 1 to a 0 and every 0 
to a 1. For example, the binary complement of “1010” is “0101”.

For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.
"""

# come back to this if we have time!
# def complement_base_10:


def main():
    # result = single_number([7, 9, 7])
    # print(result)

    print([i for i in bin(8)[2:]])
    print([(int(i) ^ 1) for i in bin(8)[2:]])


main()
