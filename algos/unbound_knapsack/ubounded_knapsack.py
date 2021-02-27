def knapsack(p, w, c):
    if len(p) == 0:
        return 0

    return knapsack_rec(p, w, c, 0, 0)


def knapsack_rec(p, w, c, i, profit):
    if c <= 0 or i >= len(p):
        return profit

    profit1 = 0
    if w[i] <= c:
        profit1 = max(profit1, knapsack_rec(p, w, c - w[i], i, profit + p[i]))

    profit2 = knapsack_rec(p, w, c, i + 1, profit)
    return max(profit1, profit2)


def main():
    p = [15, 20, 50]
    w = [1, 2, 3]
    c = 5
    result = knapsack(p, w, c)
    print(result)


main()
