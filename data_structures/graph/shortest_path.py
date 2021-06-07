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

    :param g:
    :param s:
    :return:
    """
    in_tree = {i: False for i in range(g.vertices)}
    distance = {i: float('inf') for i in range(g.vertices)}
    parent = {i: -1 for i in range(g.vertices)}

    distance[s] = 0
    v = s

    while in_tree[v] is False:
        in_tree[v] = True

        # visit all of v's neighbors, if any of them are currently recorded
        # at a greater distance than the distance from (s to v) + g.weight(v, w)
        # then update distance w to be s to v + g.weight(v, w) also update the parent
        for w in g.edges[v]:
            if distance[w] > distance[v] + g.weights[(v, w)]:
                distance[w] = distance[v] + g.weights[(v, w)]
                parent[w] = v

        # this is an mst algorithm so naturally it's copying prims vertex selection!
        v = 1
        dist = float('inf')
        for i in range(g.vertices):
            if in_tree[i] is False and dist > distance[i]:
                dist = distance[i]
                v = i

    return distance, parent


g = Graph(6)
for u, v, w in [[0, 4, 1], [0, 1, 3], [0, 2, 3], [1, 4, 1], [1, 3, 3], [3, 2, 3], [3, 4, 1], [2, 4, 1], [2, 5, 10]]:
    g.add_edge(u, v, w)

print(shortest_path_dijakstra(g, 0))
