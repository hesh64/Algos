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

        for w in g.edges[v]:
            if distance[w] > distance[v] + g.weights[(v, w)]:
                distance[w] = distance[v] + g.weights[(v, w)]
                parent[w] = v

        v = 1
        dist = float('inf')
        for i in range(g.vertices):
            if in_tree[i] is False and dist > distance[i]:
                dist = dist[i]
                v = i


