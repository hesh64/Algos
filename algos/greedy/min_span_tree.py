import heapq


class Graph:
    def __init__(self, n):
        self.n = n
        self.v = [[] for _ in range(n)]
        self.c = {}

    def insert_edge(self, s, d, c):
        self.v[s].append(d)
        self.v[d].append(s)
        self.c[(s, d)] = c
        self.c[(d, s)] = c

    def get_cost(self, s, d):
        return self.c[(s, d)]


def prims(g: Graph):
    heap = []
    g_prime = Graph(g.n)

    for u in range(g.n):
        for v in g.v[u]:
            heapq.heappush(heap, (g.get_cost(u, v), u, v))

    _, min_edge, _ = heap[0]
    visited = {min_edge}

    while heap:
        c, u, v = heapq.heappop(heap)
        if u in visited and v not in visited:
            visited.add(v)
            g_prime.insert_edge(u, v, c)

    return g_prime


if __name__ == '__main__':
    g = Graph(4)
    g.insert_edge(0, 1, 1)
    g.insert_edge(0, 3, 3)
    g.insert_edge(0, 2, 4)
    g.insert_edge(1, 3, 2)
    g.insert_edge(2, 3, 5)

    print(g.v)
    print(g.c)

    gp = prims(g)

    print(gp.v)
    print(gp.c)
