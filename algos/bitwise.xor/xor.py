def missing_number_xor(nums):
    nums.sort()

    for i in range(len(nums)):
        if (i + 1) ^ nums[i]:
            return i + 1

    return -1


"""
apparently we can do better
"""


def find_missing_number(nums):
    n = len(nums) + 1
    x1 = 1
    for i in range(2, n + 1):
        x1 = x1 ^ i

    x2 = nums[0]
    for i in range(1, n - 1):
        x2 = x2 ^ nums[i]

    return x1 ^ x2


def main():
    # for array of (n - 1)
    array = [1, 5, 2, 6, 4]
    # find the missing number, which is 3
    # one way would be to find the sum from 1 to n
    s1 = sum([i for i in range(len(array) + 1)])
    # subtract all the numbers from array
    for num in array:
        s1 -= num
    # life finds a way.
    print('the missing number is:', -s1)

    # let's put it in a function
    def missing_number(nums):
        s1 = sum([n for n in range(len(nums) + 1)])
        for num in nums:
            s1 -= num

        return -s1

    print('the missing number is:', missing_number(array))
    # what's the issue with the missing number function?
    # well we can suffer from integer overflow if the ints are too large
    # instead we can use xor
    # xor will return true for (1 ^ 0) and (0 ^ 1) and false for (1 ^ 1) and (0 ^ 0)
    print('the missing number is:', missing_number_xor(array))
    print('the missing number is:', find_missing_number(array))


main()
