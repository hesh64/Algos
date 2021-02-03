"""
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’ The goal
is to get the maximum profit out of the knapsack items. Each item can only be selected once, as we don’t have multiple
quantities of any item.

Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights
and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:

Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination as it gives us the maximum profit, and the total weight does not
exceed the capacity.
"""

"""
Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items 
which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ Each item can 
only be selected once, which means either we put an item in the knapsack or we skip it."""

import math


def solve_knapsack(profits, weights, capacity):
    max_profit = -math.inf
    max_pair = None
    for i in range(len(profits)):
        for j in range(len(profits)):
            if i != j and weights[i] + weights[j] <= capacity:
                if profits[i] + profits[j] > max_profit:
                    max_pair = [i, j]

    return max_pair


# notice this is a similar approach to the one under.
def weight_combos(weights, target, idx=0):
    if idx == len(weights):
        return [[]]

    empty = weight_combos(weights, target=target, idx=idx + 1)
    not_empty = []
    for arr in empty:
        copy = arr.copy()
        copy.append(weights[idx])
        if sum(copy) <= target:
            not_empty.append(copy)

    empty.extend(not_empty)
    return empty


# time O(2 ^ n) where n is the total number of items
def knapsack_recursive(profits, weights, capacity, idx=0):
    if capacity <= 0 or len(profits) <= idx:
        return 0

    profit1 = 0
    if weights[idx] <= capacity:
        profit1 = profits[idx] + knapsack_recursive(profits, weights, capacity - weights[idx], idx + 1)

    profit2 = knapsack_recursive(profits, weights, capacity, idx + 1)

    return max(profit1, profit2)


# O(n * c) where n is the number of items, c is the knapsack capacity
def knapsack_rec_memo(dp, profits, weights, capacity, idx):
    if capacity <= 0 or len(profits) <= idx:
        return 0

    if dp[idx][capacity] != -1:
        return dp[idx][capacity]

    profit1 = 0
    if weights[idx] <= capacity:
        profit1 = knapsack_rec_memo(dp, profits, weights, capacity - weights[idx], idx + 1)

    profit2 = knapsack_rec_memo(dp, profits, weights, capacity, idx + 1)

    dp[idx][capacity] = max(profit1, profit2)
    return dp[idx][capacity]


def knapsack_memo(profit, weights, capacity):
    dp = [[-1 for x in range(len(capacity) + 1)] for y in range(len(profit))]
    knapsack_rec_memo(dp, profit, weights, capacity, 0)


def main():
    print(knapsack_recursive([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(knapsack_recursive([1, 6, 10, 16], [1, 2, 3, 5], 6))
    # print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(weight_combos([1, 6, 10, 16], target=10))


main()
