class Graph:
    def __init__(self, n, undirected=False):
        self.vertices, self.undirected = n, undirected
        self.edges = {i: [] for i in range(n)}

    def add_edge(self, u, v):
        self.edges[u].append(v)
        if self.undirected:
            self.edges[v].append(u)


def dfs(g, pre_vertex=lambda x, y, od: None, post_vertex=lambda x, y, od: None,
        process_edge=lambda u, v, meta, od: None):
    out_degree = {i: 0 for i in range(g.vertices)}

    def dfs_helper(g, u, meta, counter):
        # there are 3 states pre, processing, and post
        a, b, c = range(3)
        # if we are not in pre state then return
        if meta[u]['c'] != a:
            return counter

        # set the start time to counter
        meta[u]['s'] = counter
        # counter ++
        counter += 1

        # we are now processing
        meta[u]['c'] = b

        # pre vertex process
        pre_vertex(u, meta, out_degree)
        for v in g.edges[u]:
            # if this edge is still preprocessing
            if meta[v]['c'] == a:
                meta[v]['p'] = u
                process_edge(u, v, meta, out_degree)
                # dfs it
                counter = dfs_helper(g, v, meta, counter)
            elif (meta[v]['c'] != b and meta[u]['p'] != v) or g.undirected is False:
                process_edge(u, v, meta, out_degree)

        # post vertex process
        post_vertex(u, meta, out_degree)

        # we have processed this vertex
        meta[u]['c'] = c
        # update the finish time with counter
        meta[u]['f'] = counter
        # counter ++
        counter += 1

        return counter

    a, b, c = range(3)

    # i represents vertex number, c color, s start, f finish, r - furthest ancestor, p direct parent
    meta = {i: {'c': a, 's': None, 'f': None, 'r': i, 'p': -1} for i in range(g.vertices)}
    counter = 1

    # for i in range(g.vertices):
    #     if meta[i]['c'] == a:
    #         counter = dfs_helper(g, i, meta, counter)
    counter = dfs_helper(g, 0, meta, counter)

    return meta


g = Graph(10, True)
edges = [[0, 1], [0, 2], [2, 3], [1, 3], [3, 4], [3, 5], [5, 6], [6, 8], [8, 9], [4, 6], [4, 7], [7, 8], [7, 9]]
for u, v in edges:
    g.add_edge(u, v)


def process_vertex_early(u, meta, out_degree):
    meta[u]['r'] = u


def process_edge(u, v, meta, out_degree):
    # an undiscovered vertex
    if meta[v]['c'] == 0:
        out_degree[u] += 1
    elif meta[v]['c'] != 0:
        if meta[v]['s'] < meta[meta[u]['r']]['s']:
            meta[u]['r'] = v


def process_vertex_late(u, meta, out_degree):
    meta_u = meta[u]
    parent = 'p'
    start = 's'
    reachable_ancestor = 'r'

    if meta[u][parent] < 0:
        if out_degree[u] > 1:
            print(f'root articulation vertex: {u}')
        return

    root = meta[meta[u][parent]][parent] < 0
    if root is not False:
        if meta[u][reachable_ancestor] == meta[u][parent]:
            print(f'parent articulation vertex: {meta[u][parent]}')

        if meta[u][reachable_ancestor] == u:
            print(f'bridge articulation vertex: {meta[u][parent]}')
            if out_degree[u] > 0:
                print(f'bridge articulation vertex: {u}')

    time_u = meta[meta[u][reachable_ancestor]][start]
    time_parent = meta[meta[meta_u[parent]][reachable_ancestor]][start]

    if time_u < time_parent:
        meta[meta_u[parent]][reachable_ancestor] = meta_u[reachable_ancestor]


meta = dfs(g, pre_vertex=process_vertex_early, process_edge=process_edge, post_vertex=process_vertex_late)

for k in meta:
    print(k, meta[k])
