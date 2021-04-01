# O(n)
def find_min_coins(v, coins_available):
    """
    This function finds the minimum number of coins
    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """

    coins = []
    coins_available.sort(reverse=True)
    j = 0
    # O(n)
    while j < len(coins_available):
        t = v // coins_available[j]
        if t > 0:
            # O(n) * V -> V is a constant, therefore, it gets dropped
            coins.extend([coins_available[j]] * t)
            v -= coins_available[j] * t
            if v == 0:
                break
        j += 1

    return coins


def main():
    v = 19
    available_coins = [1, 5, 10, 25]
    print(find_min_coins(v, available_coins))


main()
