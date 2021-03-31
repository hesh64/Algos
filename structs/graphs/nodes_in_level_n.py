class AdjNode:
    """
    A class to represent the adjacency list of the node
    """

    def __init__(self, data):
        """
        Constructor
        :param data : vertex
        """
        self.vertex = data
        self.next = None


class Graph:
    """
    Graph Class ADT
    """

    def __init__(self, vertices):
        """
        Constructor
        :param vertices : Total vertices in a graph
        """
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, source, destination):
        """
        add edge
        :param source: Source Vertex
        :param destination: Destination Vertex
        """

        # Adding the node to the source node
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

    def print_graph(self):
        """
        A function to print a graph
        """
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


def make_get_time():
    count = -1

    def get_time():
        nonlocal count
        count += 1
        return count

    return get_time


from collections import deque


def number_of_nodes(graph, level):
    """
    Calculates the number of nodes at given level
    :param graph: The graph
    :return: Total number of nodes at given level
    """

    in_degrees = {i: 0 for i in range(graph.V)}

    for i in range(graph.V):
        v = graph.graph[i]
        while v:
            in_degrees[v.vertex] += 1
            v = v.next

    source = deque()
    source.extend([k for k, v in in_degrees.items() if v == 0])
    visited = set()

    i = 0
    while source and i < level:
        i += 1
        size = len(source)
        for _ in range(size):
            u = source.popleft()
            v = graph.graph[u]
            while v:
                if v.vertex not in visited:
                    source.append(v.vertex)
                v = v.next

    return len(source)


def find_all_paths(g: Graph, s, d):
    visited = set()
    paths = []

    def helper(g: Graph, s: int, d, cur, paths, visited):
        if s in visited:
            return

        if s == d:
            c = cur.copy()
            c.append(d)
            paths.append(c)

        cur.append(s)
        visited.add(s)

        v = g.graph[s]
        while v:
            helper(g, v.vertex, d, cur, paths, visited)
            v = v.next

        cur.pop()
        visited.remove(s)

    helper(g, s, d, [], paths, visited)

    return paths


def check_if_graph_is_scc(g: Graph):
    get_time = make_get_time()
    color, start, finish = 's', 'f', 'c'
    g_info = {}
    for i in range(0, g.V):
        g_info[i] = {}
        g_info[i][start] = None
        g_info[i][finish] = None
        g_info[i][color] = 'w'

    source = 0

    def dfs_helper(g: Graph, g_info, s, tg=None):
        if tg is None:
            tg = Graph(g.V)
        g_info[s][start] = get_time()
        g_info[s][color] = 'g'

        v: AdjNode = g.graph[s]
        while v:
            tg.add_edge(v.vertex, s)
            if g_info[v.vertex][color] == 'w':
                g_info[v.vertex][color] = 'g'
                dfs_helper(g, g_info, v.vertex, tg)
            v = v.next

        g_info[s][finish] = get_time()
        g_info[s][color] = 'b'
        return tg

    gt = dfs_helper(g, g_info, source)

    smallest_final = float('inf')
    smallest_source = None
    for k, v in g_info.items():
        if v[finish] < smallest_final:
            smallest_final = v[finish]
            smallest_source = k

    stack = [smallest_source]
    visited = {smallest_source}
    while stack:
        u = stack.pop()
        v: AdjNode = gt.graph[u]
        while v:
            if v.vertex not in visited:
                visited.add(v.vertex)
                stack.append(v.vertex)
            v = v.next

    if len(visited) == g.V:
        return True

    return False


def find_all_scc(g: Graph):
    get_time = make_get_time()
    color, start, finish = 's', 'f', 'c'
    g_info = {}
    for i in range(0, g.V):
        g_info[i] = {}
        g_info[i][start] = None
        g_info[i][finish] = None
        g_info[i][color] = 'w'

    def dfs_helper(g: Graph, g_info, s, tg):
        g_info[s][start] = get_time()
        g_info[s][color] = 'g'

        v: AdjNode = g.graph[s]
        while v:
            tg.add_edge(v.vertex, s)
            if g_info[v.vertex][color] == 'w':
                g_info[v.vertex][color] = 'g'
                dfs_helper(g, g_info, v.vertex, tg)
            v = v.next

        g_info[s][finish] = get_time()
        g_info[s][color] = 'b'

    gt = Graph(g.V)
    for i in range(g.V):
        if g_info[i][color] == 'w':
            dfs_helper(g, g_info, i, gt)

    tg_info = {}
    for i in range(0, g.V):
        tg_info[i] = {}
        tg_info[i][color] = 'w'

    verts = sorted([i for i in range(g.V)], key=lambda x: g_info[x][finish], reverse=True)

    def dfs(g, g_info, s, comp):
        if g_info[s][color] != 'w':
            return
        comp.append(s)
        g_info[s][color] = 'g'
        v = g.graph[s]

        while v:
            if g_info[v.vertex][color] == 'w':
                dfs(g, g_info, v.vertex, comp)
            v = v.next

        return comp.copy()

    return [k for k in [dfs(gt, tg_info, i, []) for i in verts] if k is not None]


if __name__ == "__main__":
    V = 6  # Total vertices
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 5)
    g.add_edge(3, 5)

    print(number_of_nodes(g, 1))
    print(find_all_paths(g, 0, 5))

    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(2, 4)
    g.add_edge(4, 2)
    print(check_if_graph_is_scc(g))

    g = Graph(7)
    g.add_edge(6, 5)
    g.add_edge(5, 6)
    g.add_edge(5, 4)
    g.add_edge(4, 5)

    g.add_edge(0, 1)
    g.add_edge(1, 0)
    g.add_edge(1, 2)
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    g.add_edge(3, 0)
    g.add_edge(0, 3)

    print(find_all_scc(g))
