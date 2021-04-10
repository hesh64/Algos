class Graph:
    def __init__(self, n):
        self.vertices = n
        self.edges = [[] for _ in range(n + 1)]
        self.cost = {}

    def add_edge(self, u, v, c):
        self.edges[u].append(v)
        self.cost[(u, v)] = c

    def get_cost(self, u, v):
        return self.cost[(u, v)]


from heapq import heappush, heappop, heapify


class Vert:
    def __init__(self, key, d=float('inf'), p=None):
        self.key = key
        self.d = d
        self.p = p

    def __lt__(self, other):
        return self.d < other.d

    def __repr__(self):
        return f'({self.key}, {self.d}, {self.p})'


def dijkstra(g: Graph, s):
    def relax(u: Vert, v: Vert, c: int):
        if v.d > c + u.d:
            v.d = c + u.d
            v.p = u.key

    explored = set()
    n = g.vertices

    preprocessing = {s: Vert(s, 0)}
    for i in range(1, n + 1):
        if i != s:
            preprocessing[i] = Vert(i)

    h = list(preprocessing.values())
    heapify(h)

    while h:
        u = heappop(h)
        explored.add(u.key)
        for v_id in g.edges[u.key]:
            if v_id not in explored:
                v = preprocessing[v_id]
                relax(u, v, g.get_cost(u.key, v.key))
        heapify(h)

    return preprocessing


def main():
    g = Graph(6)
    edges = [[1, 2, 1], [1, 4, 3], [2, 3, 2], [2, 4, 1], [3, 5, 8], [4, 5, 2], [4, 6, 4], [6, 5, 1], [1, 6, 1]]
    for u, v, c in edges:
        g.add_edge(u, v, c)

    g = dijkstra(g, 1)
    for k in g:
        print(g[k])


main()
