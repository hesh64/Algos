def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes
    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """
    # O(nlogn)
    pipes.sort()
    for i in range(1, len(pipes)):
        pipes[i] += pipes[i - 1]

    return sum(pipes[1:])


def main():
    print(min_cost([4, 3, 2, 6]))


main()
