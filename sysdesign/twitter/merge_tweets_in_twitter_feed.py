def merge_tweets(feed, fl, tweets, tl):
    p1, p2 = fl - 1, tl - 1

    for p in range(fl + tl - 1, -1, -1):
        if p2 < 0:
            break

        if p1 >= 0 and feed[p1] > tweets[p2]:
            feed[p] = feed[p1]
            p1 -= 1
        else:
            feed[p] = tweets[p2]
            p2 -= 1

    return feed


def main():
    feed, fl = [11, 27, 38, 40, 55, 0, 0, 0], 5
    tweets, tl = [9, 25, 60], 3

    print(merge_tweets([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))


main()
