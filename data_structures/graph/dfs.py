class Graph:
    def __init__(self, nvertices, directed=False):
        self.nvertices = nvertices
        self.edges = {i: set() for i in range(nvertices)}

        self.directed = directed

    def add_edge(self, u, v):
        self.edges[u].add(v)
        if self.directed is False:
            self.edges[v].add(u)


"""

in undirected graphs there are two types of edges:
back edges - an edge that leads to a vertex already discovered
tree edges - an edge that's not previously discovered

in directed graphs there are 4 types of edges:
back edges - an edge that leads to a vertex already discovered
tree edges - an edge that's not previously discovered
forward edges - lead a parent to a descendents vertex
cross edges - lead a vertex to another vertex that their parent discovers

"""


def dfs(g: Graph, v, process_vertex_early=lambda u, entry_time, exit_time, parent, disc, proc, set_finished: None,
        process_edge=lambda u, v, entry_time, exit_time, parent, disc, proc, set_finished: None,
        process_vertex_late=lambda u, entry_time, exit_time, parent, disc, proc, set_finished: None,
        on_finish=lambda entry_time, exit_time, parent, disc, proc: None):
    finished = False

    def set_finished():
        nonlocal finished
        finished = True

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

        process_vertex_early(u, entry_time, exit_time, parent, disc, proc, set_finished)

        for v in g.edges[u]:
            if disc[v] is False:
                parent[v] = u
                process_edge(u, v, entry_time, exit_time, parent, disc, proc, set_finished)
                dfs_helper(v)

            elif (proc[v] is False and parent[u] != v) or g.directed is True:
                """
                this is our way of visiting backedges! we are gonna visit a previously
                discovered vertex, whos not our parent. That's literally an ancestor.
                OR OR OR OR
                if this is a directed graph that u, v and v, u are separate edges 
                """
                process_edge(u, v, entry_time, exit_time, parent, disc, proc, set_finished)

            if finished:
                return

        process_vertex_late(u, entry_time, exit_time, parent, disc, proc, set_finished)
        time = time + 1
        exit_time[u] = time

        proc[u] = True

    dfs_helper(v)

    on_finish(entry_time, exit_time, parent, disc, proc)


def articulation_vertex():
    g_template = [[0, 5], [0, 1], [0, 4], [1, 2], [2, 3], [3, 4], [4, 6]]
    nvertices = 7
    g = Graph(nvertices, False)

    for u, v in g_template:
        g.add_edge(u, v)

    print(g.edges)
    print()
    root_v = 0
    ancestor = [i for i in range(nvertices)]
    outdeg = [0] * nvertices

    # it's < than 0
    # ancestor[root_v] = -1

    def process_vertex_early(u, entry_time, exit_time, parent, disc, proc, set_finished):
        ancestor[u] = u

    def process_edge(u, v, entry_time, exit_time, parent, disc, proc, set_finished):

        if parent[v] == u:
            # print(f'{u}->{v} TREE EDGE')
            outdeg[u] += 1
        # this is very important.
        # this is where we are checking to see if a back edge to v leads to an older time
        # than our own ancestors time (we being vertex 'u')
        elif (disc[v] and not proc[v]) and parent[u] != v:
            # print(f'{u}->{v} BACK EDGE')
            if entry_time[v] < entry_time[ancestor[u]]:
                ancestor[u] = v

    # this is the second important part. Remember that the order in which this method will be calling is from
    # the node leaves at the very end of the graph all the way back to the parent
    def process_vertex_late(u, entry_time, exit_time, parent, disc, proc, set_finished):
        # check if u is a parent
        # this is the root cutnode case
        if parent[u] < 0:
            if outdeg[u] > 1:
                print(f'{u} is a root articulation vertex')
            return

        # is my parent the root?
        is_parent_root = parent[parent[u]] < 0

        if not is_parent_root:
            if ancestor[u] == parent[u]:
                print(f'{parent[parent[u]]} is a parent articulation vertex')

            if ancestor[u] == u:
                print(f'{parent[u]} is a bridge articulation vertex')

                if outdeg[u] > 0:
                    print(f'{u} is a bridge articulation vertex')

        time_v = entry_time[ancestor[u]]
        time_parent = entry_time[ancestor[parent[u]]]

        if time_v < time_parent:
            ancestor[parent[u]] = ancestor[u]

    def on_finish(entry_time, exit_time, parent, disc, proc):
        print('\n')
        for i, (e, x) in enumerate(zip(entry_time, exit_time)):
            print(f'Vertex {i}: [{e}, {x}] ancestor {i} is {ancestor[i]}')

    dfs(g, 0, on_finish=on_finish, process_vertex_early=process_vertex_early,
        process_edge=process_edge,
        process_vertex_late=process_vertex_late)


articulation_vertex()
