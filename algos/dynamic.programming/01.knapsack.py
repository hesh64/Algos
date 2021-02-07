"""Oh no here I go solving it againnnn"""


# this is a brute force solution
# def knap_sack(weights, max_weight, profit):
#     bags = [[]]
#
#     max_profit = 0
#     max_bag = []
#
#     for i, w in enumerate(weights):
#         size = len(bags)
#         for b in range(size):
#             b_copy = bags[b].copy()
#             b_copy.append(i)
#             bag_weights = [weights[i] for i in b_copy]
#             bag_profits = [profit[i] for i in b_copy]
#             if sum(bag_weights) <= max_weight:
#                 bags.append(b_copy)
#                 if sum(bag_profits) > max_profit:
#                     max_profit = sum(bag_profits)
#                     max_bag = bag_profits
#
#     return max_profit, max_bag
#
#
# let's think of this more as a tree, i wanna build a recursion tree...

def knap_sack_recursive(profits, profits_length, weights, capacity, current_index):
    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0

    # if weight of the nth item is more than Knapsack, then
    # this item can't be included in the optimal solution
    profit1 = 0

    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knap_sack_recursive(profits, profits_length, weights,
                                                               capacity - weights[current_index], current_index + 1)

    profit2 = knap_sack_recursive(profits, profits_length, weights, capacity, current_index + 1)

    return max(profit1, profit2)


def knap_sack_recursive_memo(memo, profits, profits_length, weights, capacity, current_index):
    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0

    if memo[current_index][capacity] != 0:
        return memo[current_index][capacity]

    # if weight of the nth item is more than Knapsack, then
    # this item can't be included in the optimal solution
    profit1 = 0

    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knap_sack_recursive_memo(memo, profits, profits_length, weights,
                                                                    capacity - weights[current_index],
                                                                    current_index + 1)

    profit2 = knap_sack_recursive_memo(memo, profits, profits_length, weights, capacity, current_index + 1)

    memo[current_index][capacity] = max(profit1, profit2)
    return memo[current_index][capacity]


def knap_sack(profits, profits_length, weights, capacity):
    return knap_sack_recursive(profits, profits_length, weights, capacity, 0)


def knap_sack_memo(profits, profits_length, weights, capacity):
    memo = [[0 for x in range(capacity + 1)] for x in range(profits_length + 1)]
    return knap_sack_recursive(memo, profits, profits_length, weights, capacity, 0)


def main():
    profits = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    print(knap_sack(profits, len(profits), weights, capacity))


main()
