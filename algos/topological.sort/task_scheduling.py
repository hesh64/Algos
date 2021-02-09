"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be
completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is
possible to schedule all the tasks."""

from collections import deque


# O(V + E)
# O(V + E)
def task_scheduling(tasks, prerequisites):
    ordered = []

    if tasks <= 0 and len(prerequisites) == 0:
        return True

    in_degrees = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for parent, child in prerequisites:
        graph[parent].append(child)
        in_degrees[child] += 1

    sources = deque()
    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)

    while sources:
        node = sources.popleft()
        ordered.append(node)

        for child in graph[node]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)

    return tasks == len(ordered)


def main():
    tasks, prerequisites = 3, [[0, 1], [1, 2]]
    result = task_scheduling(tasks, prerequisites)
    print(result)
    tasks, prerequisites = 3, [[0, 1], [1, 2], [2, 0]]
    result = task_scheduling(tasks, prerequisites)
    print(result)


main()
