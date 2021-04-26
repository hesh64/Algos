def min_steps(k):
    n = len(k)
    if n <= 1:
        return 0

    graph = {}
    for i in range(n):
        if k[i] not in graph:
            graph[k[i]] = []
        graph[k[i]].append(i)

    current = [0]
    visited = {0}
    steps = 0

    while current:
        next_current = []
        for node in current:
            if node == n - 1:
                return steps

            for child in graph[k[node]]:
                if child not in visited:
                    visited.add(child)
                    next_current.append(child)

            graph[k[node]].clear()

            for child in [node - 1, node + 1]:
                if 0 <= child < n and child not in visited:
                    visited.add(child)
                    next_current.append(child)

        current = next_current
        steps += 1

    return -1


def main():
    # Driver code
    k = [1, 2, 3, 4, 1, 3, 5, 3, 5]
    print(min_steps(k))


main()
