from heapq import heappush, heappop


def getOrder(tasks):
    ordered, h = [], []

    tasks = [[s, l, i] for i, [s, l] in enumerate(tasks)]
    tasks.sort()

    start = 0
    time = 0

    while start < len(tasks) or len(h):
        if len(h):
            l, index = heappop(h)
            ordered.append(index)
            time += l
        elif start < len(tasks):
            s, l, index = tasks[start]
            start += 1
            ordered.append(index)
            time = s + l

        while start < len(tasks) and tasks[start][0] <= time:
            heappush(h, [tasks[start][1], tasks[start][2]])
            start += 1

    return ordered


print(getOrder(
    [[46, 9], [46, 42], [30, 46], [30, 13], [30, 24], [30, 5], [30, 21], [29, 46], [29, 41], [29, 18], [29, 16],
     [29, 17], [29, 5], [22, 15], [22, 13], [22, 25], [22, 49], [22, 44]]))
print('\n-------\n')
