class Graph:
    def __init__(self, n):
        self.vertices = n
        self.edges = {i: set() for i in range(n)}
        self.weights = {}

    def add_edge(self, u, v, w):
        self.edges[u].add(v)
        self.edges[v].add(u)

        self.weights[(u, v)] = self.weights[(v, u)] = w


# n = vertices
# m = edges
# On^2
def shortest_path_dijakstra(g, s):
    """
    with dijakstra you're still building an mst. It's the mst of the min path
    from s to every point in the graph.


    the while loop O(V) + the edges iteration O(E) for V iterations is
    O(V + E) next we have our other v iterations to select the minimum vertex that
    only affects our V so our total time analysis is V (V + E/V) = O(V^2 + E)

    could be improved with a priority queue and a sparse enough matrix

    :param g:
    :param s:
    :return:
    """
    in_tree = {i: False for i in range(g.vertices)}
    distance = {i: float('inf') for i in range(g.vertices)}
    parent = {i: -1 for i in range(g.vertices)}

    distance[s] = 0
    v = s

    # this runs for another O(V)
    while in_tree[v] is False:
        in_tree[v] = True

        # visit all of v's neighbors, if any of them are currently recorded
        # at a greater distance than the distance from (s to v) + g.weight(v, w)
        # then update distance w to be s to v + g.weight(v, w) also update the parent
        # because we iterate over only one vertexs edges per loop and for a total of v vertexes this
        # only costs O(E)
        for w in g.edges[v]:
            # relaxing operation
            if distance[w] > distance[v] + g.weights[(v, w)]:
                distance[w] = distance[v] + g.weights[(v, w)]
                parent[w] = v

        # this is an mst algorithm so naturally it's copying prims vertex selection!
        v = 1
        dist = float('inf')
        # extract minimum vertex operation takes O(V)
        for i in range(g.vertices):
            if in_tree[i] is False and dist > distance[i]:
                dist = distance[i]
                v = i

    return distance, parent


g = Graph(6)
for u, v, w in [[0, 4, 1], [0, 1, 3], [0, 2, 3], [1, 4, 1], [1, 3, 3], [3, 2, 3], [3, 4, 1], [2, 4, 1], [2, 5, 10]]:
    g.add_edge(u, v, w)

print(shortest_path_dijakstra(g, 0))

"""
Bellman Ford
Dynamic algorithm that can detect negative back edges 
 
"""


class Graph:
    def __init__(self, n):
        self.vertices = n
        self.edges = {i: set() for i in range(n)}
        self.weights = {}

    def add_edge(self, u, v, w):
        self.edges[u].add(v)

        self.weights[(u, v)] = w

    def get_weight(self, u, v):
        if (u, v) in self.weights:
            return self.weights[(u, v)]

        return float('inf')


"""

Here we are going to treat iterating over the edges for loop 
for u in g.edges:
    for v in g.edges[v] 
    
as O(E) -- i suspect it's because of how  they get the edges or how 
the graph is defined. so with that said:

O(VE + E) => O(VE) 
"""


def bellman_ford(g, s):
    n = g.vertices

    weight = [float('inf')] * n
    parent = [0] * n

    weight[s] = 0
    # O((V-1) * E) = O(VE)
    # this is the distances portion
    for _ in range(n - 1):  # this forloop runs at V - 1 times but we can round it to V

        # this in here is |E| total work because we are iterating over every edge in the graph
        for s in g.edges:
            for d in g.edges[s]:
                if weight[d] > weight[s] + g.get_weight(s, d):
                    weight[d] = weight[s] + g.get_weight(s, d)
                    parent[d] = s

    # O(|E|) -> look at comment above the method
    # this is the checking for backcycles portion
    for s in g.edges:
        for d in g.edges[s]:
            if weight[d] > weight[u] + g.get_edges([u, v]):
                print('this is a backedge you can choose to return false here, or trace back the cycle.')

    return True
