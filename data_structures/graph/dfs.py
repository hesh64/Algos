"""
NOTE: We don't touch vertices that are disc but not processed because those are back edges that create cycles!!

"""


def dfs(g, v, process_vertex_early=lambda u, entry_time, exit_time, parent, disc, proc: False,
        process_edge=lambda u, v, entry_time, exit_time, parent, disc, proc: False,
        process_vertex_late=lambda u, entry_time, exit_time, parent, disc, proc: False):
    finished = False
    n = g.nvertices

    entry_time = [-1] * n
    exit_time = [-1] * n

    time = 0
    disc = [False] * n
    proc = [False] * n
    parent = [-1] * n

    def dfs_helper(u):
        nonlocal time, finished

        if finished:
            return

        disc[u] = True
        time += 1
        entry_time[u] = time

        finished = process_vertex_early(u, entry_time, exit_time, parent, disc, proc)
        if finished:
            return

        for v in g.edges[u]:
            if disc[v] is False:
                parent[v] = u
                finished = process_edge(u, v, entry_time, exit_time, parent, disc, proc)
                dfs_helper(v)
            # preconditions - edge v is discovered
            # here we are saying:
            #  if this is an undirected graph, we don't want to visited both (u, v) and (v, u) so if u is v's parent
            #   we are passing, which makes sense because u will not be in processed state while we visit it's children
            #
            #  else if this is a directed a graph, then (u, v) and (v, u) were set intentionally so we do visit both
            elif (proc[v] is False and parent[u] != v) or g.undirected is False:
                finished = process_edge(u, v, entry_time, exit_time, parent, disc, proc)

            if finished:
                return

        finished = process_vertex_late(u, entry_time, exit_time, parent, disc, proc)
        time = time + 1
        exit_time[u] = time

        proc[u] = True

    dfs_helper(v)


class Graph:
    def __init__(self, g, undirected=False):
        self.nvertices = len(g)
        self.edges = {i: set() for i in range(self.nvertices)}

        self.undirected = undirected

        for i in range(len(g)):
            self.edges[i] |= set(g[i])

            if undirected:
                for v in self.edges[i]:
                    self.edges[v].add(i)


g_template = [[1, 4, 5], [4, 2], [2, 3], [3, 4], [], []]
ug = Graph(g_template, True)
dfs(ug, 0)

g_template = [[1], [2], [1], [1]]
g = Graph(g_template)

for u in g.edges:
    print(u, g.edges[u])


def process_edge(u, v, entry_time, exit_time, parent, disc, proc):
    """
    this is tricky so pay close attention.

    There are two scenarios for a cycle there is a backedge to a parent
    there is a backedge to an ancestor

    if we want to detect backedges to parents -- which is the case in a directed graph. then we can include the
    second codition in the if statement right under here. because we are literatlly saying ignore, a vertex u whos
    parent is v

    the to make this work for direct graphs or with g.directed (parent[u] != v or g.directed)

    """
    if (disc[v] is True and (parent[u] != v)):
        i = v
        print('a cycle was detected from:', v, end=', ')
        while i != -1:
            i = parent[i]
            print(i, end=', ')
        print()
        return True


dfs(g, 0, process_edge=process_edge)


def top_sort(g):
    """
    this assumes the graph is connected!!

    if it's disconnected you need to iterate every undiscovered edge
    :param g:
    :return:
    """


stack = []


def process_vertex_late(v, entry_time, exit_time, parent, disc, proc):
    stack.append(v)


dfs(g, 0)

"""
somethings must still be wrong in my implementation
"""


def articulation_vertex(g, v):
    TREE, BACK, FORWARD, CROSS = range(4)
    reachable_ancestor = [0] * g.nvertices
    out_degree = [0] * g.nvertices

    def classify_edge(u, v, entry_time, exit_time, parent, disc, proc):
        if parent[v] == u:
            return TREE
        if disc[v] and proc[v] is False:
            return BACK
        if proc[v] and (entry_time[v] > entry_time[u]):
            return FORWARD
        if proc[v] and entry_time[v] < entry_time[u]:
            return CROSS

    def process_vertex_early(v, entry_time, exit_time, parent, disc, proc):
        reachable_ancestor[v] = v

    def process_edge(u, v, entry_time, exit_time, parent, disc, proc):
        cls = classify_edge(u, v, entry_time, exit_time, parent, disc, proc)
        if cls == TREE:
            out_degree[u] += 1
        if cls == BACK and parent[u] != v:
            if entry_time[v] < entry_time[reachable_ancestor[u]]:
                reachable_ancestor[u] = v

    def process_vertex_late(u, entry_time, exit_time, parent, disc, proc):
        if parent[u] < 0:
            if out_degree[u] > 1:
                print('root articulation vertex', u)
            return

        root = (parent[parent[v]] < 0)

        if root is False:
            if reachable_ancestor[u] == parent[u]:
                print('parent articulation vertex', parent[v])
            if reachable_ancestor[u] == u:
                print('bridge articulation vertex', parent[v])
                # test if v is not a leaf
                if out_degree[v] > 0:
                    print('bridge articulation vertex', v)

        time_v = entry_time[reachable_ancestor[u]]
        time_parent = entry_time[reachable_ancestor[parent[u]]]

        if time_v < time_parent:
            reachable_ancestor[parent[v]] = reachable_ancestor[u]

    dfs(g, v, process_vertex_early=process_vertex_early, process_edge=process_edge,
        process_vertex_late=process_vertex_late)


g_template = [
    [1, 2],  # 0
    [3, 0],  # 1
    [0, 3],  # 2
    [1, 2, 4, 5],  # 3
    [3, 6, 7],  # 4
    [3, 6],  # 5
    [4, 5, 8],  # 6
    [4, 8, 9],  # 7
    [6, 7, 9],  # 8
    [8, 7]  # 9
]
g = Graph(g_template, True)

articulation_vertex(g, 0)
