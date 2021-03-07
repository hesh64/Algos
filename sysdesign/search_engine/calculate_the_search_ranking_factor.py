def search_ranking(page_scores):
    length = len(page_scores)
    ranking = [0] * length
    ranking[0] = 1

    for i in range(1, length):
        ranking[i] = ranking[i - 1] * page_scores[i - 1]

    right = 1
    for i in reversed(range(length)):
        ranking[i] = ranking[i] * right
        right *= page_scores[i]

    return ranking


def main():
    page_scores = [1, 4, 6, 9]
    print(search_ranking(page_scores))

    page_scores = [3, 5, 1, 1, 6, 7, 2, 3, 4, 1, 2]
    print(search_ranking(page_scores))


main()
