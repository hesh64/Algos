from nice import *


class Graph:
    def __init__(self, n, directed=False):
        self.vertices = n
        self.edges = [set() for _ in range(n)]
        self.directed = directed

    def add_edge(self, u, v, c):
        self.edges[u].add((v, c))
        if not self.directed:
            self.edges[v].add((u, c))

    def get_edges(self):
        edges = []
        for v, s in enumerate(self.edges):
            for (u, c) in s:
                edges.append([v, u, c])

        return edges

    def _get_edges(self):
        visited = {}
        edges = []
        for u, s in enumerate(self.edges):
            for v, c in s:
                if (u, v) not in visited:
                    edges.append((u, v, c))
                    visited[(u, v)] = True
                    visited[(v, u)] = True
        return edges

    def print(self):
        # for i, s in enumerate(self.edges):
        #     print(str(i) + ':', s)

        print(self._get_edges())


def kurks_mst(g: Graph):
    # inits
    forest = UnionForest()
    mst = Graph(g.vertices)

    # preprocessing:
    for i in range(g.vertices):
        forest.make_set(i)

    # sort edges by cost min->max
    edges = sorted(g.get_edges(), key=lambda x: x[2])

    for u, v, c in edges:
        if forest.find_set(u) != forest.find_set(v):
            mst.add_edge(u, v, c)
            forest.union(v, u)
    return mst


"""
g = Graph(10)
letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
nums_to_letters = {}
for k in letters:
    nums_to_letters[letters[k]] = k

for edge in [['i', 'j', 0], ['a', 'e', 1], ['c', 'i', 1], ['e', 'f', 1], ['g', 'h', 1], ['b', 'd', 2],
             ['c', 'j', 2], ['d', 'e', 2], ['d', 'h', 2], ['a', 'd', 4], ['b', 'c', 4], ['c', 'h', 4],
             ['g', 'i', 4], ['a', 'b', 5], ['d', 'f', 5], ['h', 'i', 6], ['f', 'g', 7], ['d', 'g', 11]]:
    u, v, c = edge
    g.add_edge(letters[u], letters[v], c)

g.print()
print(g.get_edges())

print('\n\n')
mst = kurks_mst(g)
print('\n\n')
edges = []
for u, v, c in mst._get_edges():
    edges.append((nums_to_letters[u], nums_to_letters[v], c))

edges.sort(key=lambda x: x[2])
for e in edges:
    print(e)
"""

g = Graph(5)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 1)
g.add_edge(0, 3, 2)
g.add_edge(0, 4, 5)
g.add_edge(2, 3, 1)
g.add_edge(4, 3, 1)

g.print()

mst = kurks_mst(g)
mst.print()
