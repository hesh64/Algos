from collections import deque


def total_time(main_server_id, parents, delays):
    n = len(parents)
    graph = {i: [] for i in range(n)}

    for i, val in enumerate(parents):
        if val not in graph:
            graph[val] = []
        graph[val].append(i)

    s = 0
    q = deque()
    q.append([main_server_id, delays[main_server_id]])
    while q:
        cur_id, cur_delay = q.popleft()
        s = max(s, cur_delay)
        for child in graph[cur_id]:
            q.append([child, cur_delay + delays[child]])
    return s


def main():
    main_server_id = 0
    parents = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    delays = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

    print(total_time(main_server_id, parents, delays))


main()
