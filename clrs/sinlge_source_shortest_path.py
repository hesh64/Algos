class Graph:
    def __init__(self, n, edges):
        self.size = n
        self.vertices = {}
        for i in range(1, n + 1):
            self.vertices[i] = []

        self.weights = {}

        for s, d, w in edges:
            self.vertices[s].append(d)
            self.weights[(s, d)] = w

    def get_weight(self, s, d):
        return self.weights[(s, d)]

    def insert(self, s, d, w):
        self.vertices[s].append(d)
        self.weights[(s, d)] = w


def init_graph(g, s):
    properties = {}
    for i in range(1, g.size + 1):
        properties[i] = {
            'd': float('inf'),
            'p': None
        }

    properties[s]['d'] = 0
    return properties


def relax(gp, u, v, w):
    if gp[v]['d'] > gp[u]['d'] + w:
        gp[v]['d'] = gp[u]['d'] + w
        gp[v]['p'] = u


# O(V * E)
def bellman_ford(g: Graph, s: int):
    # O(V)
    gp = init_graph(g, s)

    # O((V - 1) * E)
    for _ in range(g.size - 1):
        for u in g.vertices:
            for v in g.vertices[u]:
                relax(gp, u, v, g.get_weight(u, v))

    # O(E)
    for u in g.vertices:
        for v in g.vertices[u]:
            # if get_wight is negative this condition will be true
            # and the cycle is detected.
            if gp[v]['d'] > gp[u]['d'] + g.get_weight(u, v):
                return False

    return True


def topological_sort(g: Graph):
    in_degrees = {i: 0 for i in range(1, g.size + 1)}
    for u in g.vertices:
        for v in g.vertices[u]:
            in_degrees[v] += 1

    # print(in_degrees)

    mothers = []
    for k in in_degrees:
        if in_degrees[k] == 0:
            mothers.append(k)

    ordered = []
    while mothers:
        u = mothers.pop(0)
        ordered.append(u)

        for v in g.vertices[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                mothers.append(v)

    return ordered


# O(V + E)
def shortest_paths_in_dag(g: Graph, s):
    ordered = topological_sort(g)
    gp = init_graph(g, s)
    for u in ordered:
        for v in g.vertices[u]:
            relax(gp, u, v, g.get_weight(u, v))

    return [[v['p'], k, v['d']] for k, v in gp.items() if v['p'] is not None]


def main():
    edges = [[1, 2, 6], [1, 5, 7], [2, 3, 5], [2, 5, 8], [2, 4, -4], [3, 2, -2], [4, 1, 2], [4, 3, 7], [5, 4, 9],
             [5, 3, -3]]

    g = Graph(5, edges)
    shortest = bellman_ford(g, 1)
    print(shortest)

    # 6 verts
    edges = [[1, 2, 5], [1, 3, 3], [2, 3, 2], [2, 4, 6], [3, 4, 7], [3, 5, 4], [3, 6, 2], [4, 5, -1], [4, 6, 1],
             [5, 6, -2]]
    g = Graph(6, edges)
    shortest = shortest_paths_in_dag(g, 2)
    print(shortest)


main()
