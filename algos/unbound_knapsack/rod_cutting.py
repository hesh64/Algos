"""
Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that
will maximize the profit. We are also given the price of every piece of length ‘i’
where ‘1 <= i <= n’.

Example:

Lengths: [1, 2, 3, 4, 5]
Prices: [2, 6, 7, 10, 13]
Rod Length: 5

Let’s try different combinations of cutting the rod:

Five pieces of length 1 => 10 price
Two pieces of length 2 and one piece of length 1 => 14 price
One piece of length 3 and two pieces of length 1 => 11 price
One piece of length 3 and one piece of length 2 => 13 price
One piece of length 4 and one piece of length 1 => 12 price
One piece of length 5 => 13 price

This shows that we get the maximum price (14) by cutting the rod into two pieces of length ‘2’ and one
piece of length ‘1’.
"""


def rod_cutting(lengths, prices, length):
    if len(lengths) == 0 or length == 0 or len(prices) == 0:
        return 0

    return rot_cutting_rec(lengths, prices, length, 0, 0)


def rot_cutting_rec(lengths, prices, length, index, profits):
    if index >= len(lengths) or length == 0:
        return profits

    profit1 = 0

    if lengths[index] <= length:
        profit1 = rot_cutting_rec(lengths, prices, length - lengths[index], index, profits + prices[index])

    profit2 = rot_cutting_rec(lengths, prices, length, index + 1, profits)

    return max(profit1, profit2)


def main():
    lengths = [1, 2, 3, 4, 5]
    prices = [2, 6, 7, 10, 13]
    length = 5

    result = rod_cutting(lengths, prices, length)
    print(result)


main()
