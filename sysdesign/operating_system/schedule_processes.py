from collections import deque


def schedule(tasks, n):
    if n <= 0:
        return []

    graph = {i: [] for i in range(1, n + 1)}
    in_degrees = {i: 0 for i in range(1, n + 1)}

    # great the graph, and in_degrees
    for parent, child in tasks:
        graph[parent].append(child)
        in_degrees[child] += 1

    # find 0 in_degrees
    que = deque()
    for key in in_degrees:
        if in_degrees[key] == 0:
            que.append(key)

    sorted = []
    while que:
        node = que.popleft()
        sorted.append(node)
        for child in graph[node]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                que.append(child)
    if len(sorted) != n:
        return []

    return sorted


def main():
    tasks, n = [[6, 4], [4, 1], [1, 2], [2, 3], [4, 5], [6, 5], [5, 3]], 6
    print(schedule(tasks, n))


main()
