"""
There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses. The only
restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the security system.
How should the thief maximize his stealing?

Problem Statement #
Given a number array representing the wealth of ‘n’ houses, determine the maximum amount of money the thief can
steal without alerting the security system.
"""


def house_thief(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]

    return house_thief_rec(array, 0)


def house_thief_rec(array, i):
    if i >= len(array):
        return 0

    profit1 = array[i] + house_thief_rec(array, i + 2)
    profit2 = house_thief_rec(array, i + 1)
    return max(profit1, profit2)


def house_thief_mem(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]

    dp = [-1 for _ in range(len(array))]

    return house_thief_rec_memo(dp, array, 0)


def house_thief_rec_memo(dp, array, i):
    if i >= len(array):
        return 0

    if dp[i] == -1:
        profit1 = array[i] + house_thief_rec_memo(dp, array, i + 2)
        profit2 = house_thief_rec_memo(dp, array, i + 1)
        dp[i] = max(profit1, profit2)

    return dp[i]


def main():
    result = house_thief([2, 5, 1, 3, 6, 2, 4])
    print(result)
    result = house_thief([2, 10, 14, 8, 1])
    print(result)

    result = house_thief_mem([2, 5, 1, 3, 6, 2, 4])
    print(result)
    result = house_thief_mem([2, 10, 14, 8, 1])
    print(result)


main()
