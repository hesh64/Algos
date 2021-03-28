from heapq import *


class Graph:
    def __init__(self, n, edges):
        self.size = n
        self.vertices = {}
        for i in range(1, n + 1):
            self.vertices[i] = []

        self.weights = {}

        for s, d, w in edges:
            self.vertices[s].append(d)
            self.vertices[d].append(s)
            self.weights[(s, d)] = w
            self.weights[(d, s)] = w
            # self.weights[str(d) + ':' + str(s)] = w

    def get_weight(self, s, d):
        return self.weights[(s, d)]

    def insert(self, s, d, w):
        self.vertices[s].append(d)
        self.weights[(s, d)] = w


# O(E lg V)
def mst_kruskal(g):
    # O(1)
    a = set()

    vert_to_set = {}

    # step 1 make a set with all vertices
    # this choice of set implementation is what affects the runtime directly
    # utilizing a disjoint set forest would be the faster way. Def something
    # to circle back to.
    # O(V)
    for i in range(1, g.size + 1):
        vert_to_set[i] = set()
        vert_to_set[i].add(i)

    # step 2 get the weight sorted vertex paris
    # O(E lg E)
    weights = sorted([[k, v] for k, v in g.weights.items()], key=lambda x: x[1])

    # step 3 we want to connect the cheapest parts first
    # that are not already connected
    # O(E)
    for (u, v), w in weights:
        # by checking that two vertices are not part of the same
        # set, we know that we can connect them
        if vert_to_set[u] != vert_to_set[v]:
            a.add((u, v, w))
            union = vert_to_set[u].union(vert_to_set[v])
            for vert in union:
                vert_to_set[vert] = union

    return sorted(list(a), key=lambda x: x[2])


class Vertex:
    def __init__(self, index):
        self.index = index
        self.children = []
        self.visited = False

    def __repr__(self):
        return f'{self.index} {self.children if len(self.children) else ""}'


# O(E lg V)
def mst_prims(g, r):
    vertices = {}
    heap = []
    vert_count = 0

    for i in range(1, g.size + 1):
        vertices[i] = Vertex(i)

    u = vertices[r]
    i = 0
    edges = []

    while i < g.size:
        u.visited = True
        vert_count += 1
        min_neighbor = None

        for v_index in g.vertices[u.index]:
            if min_neighbor is None:
                min_neighbor = v_index
            elif g.get_weight(u.index, v_index) < g.get_weight(u.index, min_neighbor):
                min_neighbor = v_index
            heappush(heap, (g.get_weight(u.index, v_index), u.index, v_index))

        while len(heap):
            w, u_index, v_index = heappop(heap)
            if vertices[u_index].visited is True and vertices[v_index].visited is False:
                edges.append([u_index, v_index, w])
                u = vertices[v_index]
                break

        i += 1

    return sorted(edges, key=lambda x: x[2])


def main():
    edges = [[1, 2, 4], [2, 3, 8], [3, 4, 7], [4, 5, 9],
             [4, 6, 14], [5, 6, 10], [3, 6, 4], [6, 7, 2],
             [7, 8, 1], [7, 9, 6], [1, 8, 8], [2, 8, 11],
             [3, 9, 2], [8, 9, 7]]

    g = Graph(9, edges)

    print('kruskal')
    mst = mst_kruskal(g)
    print(mst)

    print('\n\nprim')
    mst = mst_prims(g, 1)
    print(mst)


main()
