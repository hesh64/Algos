def least_time(stocks, s_time):
    # calc frequencies
    freq = [0] * 26
    for s in stocks:
        freq[s - ord('A')] += 1

    freq.sort()
    f_max = freq.pop()
    idle_interval = (f_max - 1) * s_time

    while freq and idle_interval > 0:
        idle_interval -= min(f_max - 1, freq.pop())

    if idle_interval > 0:
        return idle_interval + len(stocks)
    else:
        len(stocks)


def main():
    # Driver code
    transaction = ['A', 'A', 'A', 'T', 'T', 'M', 'A']
    k = 2

    print("Time requires to trade all stocks:", least_time(transaction, k), "intervals")


main()
