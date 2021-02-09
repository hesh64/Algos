from collections import deque


def topological_sort(vertices, edges):
    sorted_order = []
    if vertices <= 0:
        return sorted_order

    # 1 initialize the graph
    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    # build the graph
    for edge in edges:
        parent, child = edge
        graph[parent].append(child)
        in_degree[child] += 1

    # find all sources i.e. all vertices  with 0 in-degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # deque the sources and push any of their children who now dropped to degree 0
    while sources:
        source = sources.popleft()
        sorted_order.append(source)
        for child in graph[source]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # topological order is not possible as the graph has a cycle
    if len(sorted_order) != vertices:
        return []

    return sorted_order


def main():
    vertices, edges = 4, [[3, 2], [3, 0], [2, 0], [2, 1]]
    result = topological_sort(vertices, edges)
    print(result)


main()
