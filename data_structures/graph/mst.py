import heapq


class Graph:
    def __init__(self, n):
        self.vertices = n
        self.edges = {i: set() for i in range(n)}
        self.weights = {}

    def add_edge(self, u, v, w):
        self.edges[u].add(v)
        self.edges[v].add(u)

        self.weights[(u, v)] = self.weights[(v, u)] = w


class UnionSet:
    def __init__(self, x):
        self.x = x
        self.p = self
        self.r = 0


class UnionForest:
    def __init__(self):
        self.sets = {}

    def make_set(self, x):
        if x not in self.sets:
            self.sets[x] = UnionSet(x)

    def union_find(self, x):
        if self.sets[x] != self.sets[x].p:
            self.sets[x].p = self.union_find(self.sets[x].p.x)

        return self.sets[x].p.x

    def union(self, x, y):
        if self.union_find(x) != self.union_find(y):
            self.link(x, y)

    def link(self, x, y):
        if self.sets[x].r > self.sets[y].r:
            self.sets[y].p = self.sets[x]
        else:
            self.sets[x].p = self.sets[y]
            if self.sets[x].r == self.sets[y].r:
                self.sets[y].r += 1


g = Graph(6)
for u, v, w in [[0, 4, 1], [0, 1, 3], [0, 2, 3], [1, 4, 1], [1, 3, 3], [3, 2, 3], [3, 4, 1], [2, 4, 1], [2, 5, 10]]:
    g.add_edge(u, v, w)


# n = vertices
# m = edges
# On^2 implementation
def prims_mst(g, s):
    mst = Graph(g.vertices)
    in_tree = {i: False for i in range(g.vertices)}
    distance = {i: float('inf') for i in range(g.vertices)}
    parent = {i: -1 for i in range(g.vertices)}

    distance[s] = 0
    v = s

    while in_tree[v] is False:
        in_tree[v] = True

        for w in g.edges[v]:
            if distance[w] > g.weights[(v, w)] and in_tree[w] is False:
                distance[w] = g.weights[(v, w)]
                parent[w] = v

        v = 1
        dist = float('inf')
        for i in range(g.vertices):
            if in_tree[i] is False and dist > distance[i]:
                dist = distance[i]
                v = i

    print(distance, parent)

    for k in parent:
        if parent[k] != -1:
            mst.add_edge(k, parent[k], distance[k])
    return mst


# O(m + nlgn) implementation
def prims_mst_heap(g):
    mst = Graph(g.vertices)
    in_mst = {0}

    # upper bound of o(m)
    h = [(g.weights[(0, v)], 0, v) for v in g.edges[0]]
    # upper bound of o(m)
    heapq.heapify(h)

    # iterating over all the edges then nlogn work over the entire time that O(m + nlogn)
    while len(in_mst) != g.vertices or len(h) == 0:
        w, u, v = heapq.heappop(h)

        # this will run at most nlogn because you depend on in_mst
        if u in in_mst and v not in in_mst:
            in_mst.add(v)
            mst.add_edge(u, v, w)
            for vi in g.edges[v]:
                # log(n) the most you will insert into the heap, depends on how many vertices are in mst
                # this has an upper bound of n so logn to insert into the heap
                if vi not in in_mst:
                    heapq.heappush(h, (g.weights[(v, vi)], v, vi))

    return mst


mstg = prims_mst(g, 0)
seen = set()
for u in range(mstg.vertices):
    for v in mstg.edges[u]:
        if (u, v) not in seen and (v, u) not in seen:
            print(u, v, mstg.weights[(u, v)])
            seen.add((u, v))

print('-')

g = Graph(5)
for u, v, w in [[0, 4, 1], [0, 1, 3], [0, 2, 3], [1, 4, 1], [1, 3, 3], [3, 2, 3], [3, 4, 1], [2, 4, 1]]:
    g.add_edge(u, v, w)


def kurk_mst(g):
    edges = []
    forest = UnionForest()
    for u in range(g.vertices):
        forest.make_set(u)
        for v in g.edges[u]:
            edges.append((g.weights[(u, v)], u, v))

    edges.sort(key=lambda x: x[0])
    edges.reverse()

    mst = Graph(g.vertices)
    unions = 0

    while edges and unions < g.vertices - 1:
        w, u, v = edges.pop()
        if forest.union_find(u) != forest.union_find(v):
            forest.union(u, v)
            unions += 1
            mst.add_edge(u, v, w)

    return mst


mstg = kurk_mst(g)
seen = set()
for u in range(mstg.vertices):
    for v in mstg.edges[u]:
        if (u, v) not in seen and (v, u) not in seen:
            print(u, v, mstg.weights[(u, v)])
            seen.add((u, v))
