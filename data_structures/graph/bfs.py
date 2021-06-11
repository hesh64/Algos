from collections import deque
from typing import List


class Graph:
    def __init__(self, n, undirected=False):
        self.nvertices = n
        self.undirected = undirected

        self.edges = {i: set() for i in range(n)}

    def add_edge(self, u, v):
        self.edges[u].add(v)

        if self.undirected:
            self.edges[v].add(u)


def bfs(g, start,
        process_vertex_early=lambda u: None,
        process_edge=lambda u, v: None,
        process_vertex_late=lambda u: None,
        ):
    # initialize search
    n = g.nvertices
    processed = [False] * n
    discovered = [False] * n
    parent = [-1] * n

    q = deque()

    discovered[start] = True
    q.append(start)

    while q:
        u = q.popleft()

        process_vertex_early(u)
        processed[u] = True

        for v in g.edges[u]:
            if processed[v] is False or g.undirected is False:
                process_edge(u, v)
            if discovered[v] is False:
                q.append(v)
                discovered[v] = True
                parent[v] = u

        process_vertex_late(u)

    return parent


""" 
a , or ' makes the tail of the edge

   1 -> 2 -> 3 ,_ 
 ,/ \ ,_____/ '|  \
 0   7         6   \
 |,_/ '\ _____/'    8
 4      5        
 
 in bfs we should go from 
 0 to 1, 4
 from 1 to 2, 7
 from 4 to 7
 from 2 to 3
 from 7 to 5, 3
 from 3 to 6, 8
 from 6 to 5
"""
edges = [[0, 1], [0, 4], [1, 2], [1, 7], [2, 3], [3, 6], [3, 8], [4, 7], [7, 5], [7, 3], [6, 5], ]
g = Graph(9)

for u, v in edges:
    g.add_edge(u, v)

parent = bfs(g, 0,
             process_vertex_early=lambda u: print('process vertex early', u),
             process_edge=lambda u, v: print('process edge', u, v),
             process_vertex_late=lambda u: print('process vertex early', u),
             )
print([c for p, c in sorted([(parent[c], c) for c in range(len(parent))], key=lambda x: x[0])])


def bfs_order_in_directed_graph(g, s):
    in_edges = [0 for _ in range(g.nvertices)]
    for u in range(g.nvertices):
        for v in g.edges[u]:
            in_edges[v] += 1

    q = deque()
    q.append(s)
    parents = []
    while q:
        u = q.pop()
        parents.append(u)

        for v in g.edges[u]:
            in_edges[v] -= 1
            if in_edges[v] == 0:
                q.append(v)

    if len(parents) != len(in_edges):
        return -1
    return parents


print(bfs_order_in_directed_graph(g, 0))


def is_bipartite(g: List[List[int]]) -> bool:
    f = [None] * len(g)

    def bfs(g, s, pve=lambda u: None, pe=lambda u, v: None, pvl=lambda u: None):
        parent = [-1] * len(g)
        disc = [False] * len(g)
        proc = [False] * len(g)

        q = deque()
        q.append(s)

        disc[s] = True

        while q:
            u = q.pop()

            pve(u)
            proc[u] = True

            for v in g[u]:
                if proc[v] is False:
                    pe(u, v)
                if disc[v] is False:
                    disc[v] = True
                    q.append(v)
                    parent[v] = u

            pvl(u)

    bipartite = True

    def process_edge(u, v):
        nonlocal bipartite
        if not bipartite:
            return

        if f[v] == f[u]:
            bipartite = False

        else:
            f[v] = not f[u]

    for i in range(len(f)):
        if f[i] is None:
            s = i
            f[s] = True
            bfs(g, i, pe=process_edge)
        if bipartite is False:
            return bipartite
    return bipartite


gs = [[[1], [0], [4], [4], [2, 3]],
      [[4], [], [4], [4], [0, 2, 3]],
      [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]],
      [[1, 3], [0, 2], [1, 3], [0, 2]],
      [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5,
                                                                                                                6, 7,
                                                                                                                8]], ]
for g in gs:
    print(is_bipartite(g))
