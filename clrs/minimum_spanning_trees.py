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
            # self.weights[str(d) + ':' + str(s)] = w

    def get_weight(self, s, d):
        return self.weights[(s, d)]

    def insert(self, s, d, w):
        self.vertices[s].append(d)
        self.weights[(s, d)] = w


def mst_kruskal(g):
    a = set()

    vert_to_set = {}

    # step 1 make a set with all vertices
    for i in range(1, g.size + 1):
        print(i)
        vert_to_set[i] = set()
        vert_to_set[i].add(i)

    # step 2 get the weight sorted vertex paris
    weights = sorted([[k, v] for k, v in g.weights.items()], key=lambda x: x[1])

    # step 3 we want to connect the cheapest parts first
    # that are not already connected
    for (u, v), w in weights:
        # by checking that two vertices are not part of the same
        # set, we know that we can connect them
        if vert_to_set[u] != vert_to_set[v]:
            a.add((u, v, w))
            union = vert_to_set[u].union(vert_to_set[v])
            for vert in union:
                vert_to_set[vert] = union

    return sorted(list(a), key=lambda x: x[2])


def main():
    edges = [[1, 2, 4], [2, 3, 8], [3, 4, 7], [4, 5, 9],
             [4, 6, 14], [5, 6, 10], [3, 6, 4], [6, 7, 2],
             [7, 8, 1], [7, 9, 6], [8, 1, 8], [2, 8, 11],
             [3, 9, 2], [8, 9, 7]]

    g = Graph(9, edges)
    mst = mst_kruskal(g)
    print(mst)


main()
