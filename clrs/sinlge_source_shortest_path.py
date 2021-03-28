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


def relax(u, v, w):
    if v['d'] > u['d'] + w:
        v['d'] = u['d'] + w
        v['p'] = u


# O(V * E)
def bellman_ford(g: Graph, s: int):
    # O(V)
    gp = init_graph(g, s)

    # O((V - 1) * E)
    for _ in range(g.size - 1):
        for u in g.vertices:
            for v in g.vertices[u]:
                relax(gp[u], gp[v], g.get_weight(u, v))

    # O(E)
    for u in g.vertices:
        for v in g.vertices[u]:
            # if get_wight is negative this condition will be true
            # and the cycle is detected.
            if gp[v]['d'] > gp[u]['d'] + g.get_weight(u, v):
                return False

    return True


def main():
    edges = [[1, 2, 6], [1, 5, 7], [2, 3, 5], [2, 5, 8], [2, 4, -4], [3, 2, -2], [4, 1, 2], [4, 3, 7], [5, 4, 9],
             [5, 3, -3]]

    g = Graph(5, edges)
    shortest = bellman_ford(g, 1)
    print(shortest)


main()
