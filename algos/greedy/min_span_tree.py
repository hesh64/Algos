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


class UnionSet:
    def __init__(self):
        self.set = dict()

    def set(self, k, val):
        self.set[k] = val


# O(M * N) -> O(|V| * |E|)
def prims(g: Graph):
    heap = []
    g_prime = Graph(g.n)
    u = 0
    visited = {u}

    for v in g.v[u]:
        # we want to filter out the (u,v) (v, u) reverse edges
        heapq.heappush(heap, (g.get_cost(u, v), u, v))

    i = 0
    while i < g.n:
        c, u, v = heapq.heappop(heap)
        if u in visited and v not in visited:
            visited.add(v)
            g_prime.insert_edge(u, v, c)

            for p in g.v[v]:
                if p not in visited:
                    heapq.heappush(heap, (g.get_cost(v, p), v, p))
        i += 1
    return g_prime


class DisjointItem:
    def __init__(self, key):
        self.key = key
        self.rank = 0
        self.p = self

    def __repr__(self):
        return f'{(self.key, self.rank)} -> {self.p if self.p != self else "Circulates"}'


# O(M alpha n)
class DisjointSetForest:
    def __init__(self):
        self.sets = set()

    def make_set(self, x):
        ds = DisjointItem(x)
        ds.p = ds
        ds.rank = 0
        self.sets.add(ds)
        return ds

    def find_set(self, x: DisjointItem):
        # secret sauce 2: on the way back from checking who your parent is, we'll update your .p pointer
        # to show he is your oldest ancestor! such that you your parent and siblings end up pointing
        # to the same object.
        if x.p != x:
            # on the way back from the top, your assigning the final parent to every node
            x.p = self.find_set(x.p)

        return x.p

    # Secret Sauce 1: Union by rank, if you have a lower rank you're automatically the child
    def link(self, x, y):
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank += 1

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))


def kur(g: Graph):
    forest = DisjointSetForest()
    sets = {}
    edges = []
    for u in range(g.n):
        sets[u] = forest.make_set(u)
        for v in g.v[u]:
            edges.append((u, v, g.get_cost(u, v)))

    edges.sort(key=lambda x: x[2])

    a = set()

    for u, v, c in edges:
        if forest.find_set(sets[u]) != forest.find_set(sets[v]):
            a.add((u, v, c))
            forest.union(sets[u], sets[v])

    for k in sets:
        print(sets[k].p)
    print(a)
    print(sum(s[2] for s in a))
    print('end----')


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
    kur(g)

    print(gp.v)
    print(gp.c)

    print(g.v)
    print(g.c)

    print('\n\n')
    g = Graph(4)
    g.insert_edge(0, 1, 1)
    g.insert_edge(0, 2, 2)
    g.insert_edge(2, 3, 4)
    g.insert_edge(0, 3, 3)
    # g.insert_edge(2, 3, 5)

    print(g.v)
    print(g.c)

    # gp = prims(g)
    kur(g)

    print('\n\n')
    g = Graph(7)
    for u, v, c in [[2, 1, 87129], [3, 1, 14707], [4, 2, 34505], [5, 1, 71766], [6, 5, 2615], [7, 2, 37352]]:
        g.insert_edge(u - 1, v - 1, c)
    # g.insert_edge(0, 2, 2)
    # g.insert_edge(2, 3, 4)
    # g.insert_edge(0, 3, 3)
    # g.insert_edge(2, 3, 5)

    print(g.v)
    print(g.c)

    # gp = prims(g)
    kur(g)
    #
    # print(gp.v)
    # print(gp.c)
    #
    # print(g.v)
    # print(g.c)
