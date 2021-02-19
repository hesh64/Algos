from collections import deque


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        if self.value is None:
            return ''
        return f'{self.value} -> {self.next}'


class LinkedList:
    def __init__(self):
        self.head_node = None

    def __len__(self):
        if self.head_node is None:
            return 0

        cur = self.head_node
        count = 0

        while cur:
            count += 1
            cur = cur.next

        return count

    def get_head(self):
        return self.head_node

    def is_empty(self):
        return len(self) == 0

    def insert_at_head(self, value):
        new_head = Node(value)
        new_head.next = self.head_node
        self.head_node = new_head

        return True

    def delete(self, value):
        if not self.is_empty():
            if self.head_node.value == value:
                self.head_node = self.head_node.next
                return True

        cur = self.head_node
        while cur.next:
            if cur.next.value == value:
                cur.next = cur.next.next
                return True

        return False

    def __repr__(self):
        if self.head_node is None:
            return ''

        return f'{self.head_node}'


class Graph:
    def __init__(self, vertices, directed=True):
        self.vertices = vertices
        self.array = []
        self.directed = directed

        for _ in range(vertices):
            self.array.append(LinkedList())

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_head(destination)
            if not self.directed:
                self.array[destination].insert_at_head(source)

            return True
        return False

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        print('')
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.value, end=" ] -> ")
                temp = temp.next
            print("None")


# O(v + e)
def bfs(graph, source):
    returned = []
    visited = {}
    q = deque()
    q.append(source)

    while q:
        vert = q.popleft()
        returned.append(vert)
        visited[vert] = True
        cur = graph.array[vert].get_head()
        while cur:
            if cur.value not in visited:
                q.append(cur.value)

            cur = cur.next

    return returned


# O(V + E)
def dfs(graph, source):
    returned = []
    visited = {}
    q = deque()
    q.append(source)
    while q:
        vert = q.pop()
        returned.append(vert)
        visited[vert] = True
        cur = graph.array[vert].get_head()
        while cur:
            if cur.value not in visited:
                q.append(cur.value)
            cur = cur.next

    return returned


"""
The concept of loops or cycles is very common in graph theory. A cycle exists when you traverse the directed 
graph and come upon a vertex that has already been visited.

You have to implement the detect_cycle function which tells you whether or not a graph contains a cycle.
"""


def find_cycle_rec(g, ver, visited, stack):
    if stack[ver]:
        return True

    # we have been here, and made it out, so clearly not cyclic
    if visited[ver]:
        return False

    stack[ver] = True
    visited[ver] = True

    cur = g.array[ver].get_head()
    while cur:
        if find_cycle_rec(g, cur.value, visited, stack):
            return True
        cur = cur.next

    # we made it out of the recursion
    # we are popping this frame off the stack
    stack[ver] = False
    return False


# O(V + E)
def find_cycle(g):
    if g.vertices < 1:
        return False

    visited, stack = [False] * g.vertices, [False] * g.vertices

    for vert in range(g.vertices):
        if find_cycle_rec(g, vert, visited, stack):
            return True

    return False


"""
You have to implement the find_mother_vertex() function which will take a directed graph as an input and find out
 which vertex is the mother vertex in the graph.

By definition, the mother vertex is a vertex in a graph such that all other vertices in a graph can be reached by 
following a path from that vertex. A graph can have multiple mother vertices, but you only need to find one.

"""


# O(V(V + E))
# find mother vertex brute force
def find_mother(g):
    num_of_verts = g.vertices
    sources = []
    for source in range(num_of_verts):
        visited_count = find_mother_rec(g, source)
        if visited_count == num_of_verts:
            sources.append(source)

    return sources


def find_mother_rec(g, source):
    num_of_visited = 0
    visited = [False] * g.vertices

    stack = deque()
    stack.append(source)
    visited[source] = True

    while stack:
        vert = stack.pop()
        cur = g.array[vert].get_head()

        while cur:
            if visited[cur.value] is False:
                stack.append(cur.value)
                visited[cur.value] = True
                num_of_visited += 1
            cur = cur.next

    return num_of_visited + 1


# O(V + E) it's a whole V less than the brute force solution
def find_mother_kosaraju(g):
    visited = [False] * g.vertices
    # this will be mother
    last_v = None

    for vert in range(g.vertices):
        if visited[vert] is False:
            dfs_kosaraju(g, vert, visited)
            last_v = vert

    visited = [False] * g.vertices
    dfs_kosaraju(g, last_v, visited)

    if any(vertex is False for vertex in visited):
        return -1
    else:
        return last_v


def dfs_kosaraju(g, source, visited):
    visited[source] = True
    stack = deque()
    stack.append(source)

    while stack:
        vert = stack.pop()
        cur = g.array[vert].get_head()
        while cur:
            if visited[cur.value] is False:
                visited[cur.value] = True
                stack.append(cur.value)

            cur = cur.next


"""
You have to implement the num_edges() function which takes an undirected graph and computes the total number of 
bidirectional edges. An illustration is also provided for your understanding.

"""


# O(V+E)
# count the number of edges in a unidirected graph
def num_edges(g):
    sum = 0
    for i in range(g.vertices):
        cur = g.array[i].get_head()
        while cur:
            sum += 1
            cur = cur.next
    return sum // 2


"""
You have to implement the check_path() function. It takes a source vertex and a destination vertex and tells us
 whether or not a path exists between the two.

"""


def check_path(g, source, destination):
    if source == destination:
        return True

    cur = g.array[source].get_head()
    while cur:
        if cur.value == destination or check_path(g, cur.value, destination):
            return True

        cur = cur.next

    return False


"""
The next section will tackle the tree data structure. For now, here’s the basic difference between a graph and a tree.
 A graph can only be a tree under two conditions:

There are no cycles.
The graph is connected
"""


def check_cycle(g, node, visited, parent):
    visited[node] = True

    cur = g.array[node].get_head()
    while cur:
        if visited[cur.value] is False:
            if check_cycle(g, cur.value, visited, node) is True:
                return True

        # you cant equal a visited item, and not be the parent!
        # not in this graph you wont!
        elif cur.data is not parent:
            return True

    return False


def is_tree(g):
    visited = [False] * g.vertices

    if check_cycle(g, 0, visited, -1):
        return False

    if any(i is False for i in visited):
        return False

    return True


"""
Implement the find_min() function which will take a directed graph and two vertices, A and B. The result will be the
shortest path from A to B.

Remember, the shortest path will contain the minimum number of edges.

"""


# O(V + E)
def get_min_length_path(g, source, destination):
    min_len = float('inf')

    def dfs(g, s, d, le=0):
        nonlocal min_len
        if s == d:
            min_len = min(min_len, le)
            return

        cur = g.array[source].get_head()
        while cur:
            dfs(g, cur.value, destination, le + 1)
            cur = cur.next

    dfs(g, source, destination, 0)
    return min_len


"""You must implement the remove_edge function which takes a source and a destination as arguments. If an edge  
between the two, it should be deleted."""


# O(E) because you can have all the edges sitting between the two nodes
def delete_edge(g, s, d):
    if len(g.array) == 0:
        return False

    if 0 <= s < g.vertices and 0 <= d < g.vertices:
        g.array[s].delete(d)

    return g


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    # g.add_edge(4, 1) # enable to get find_cycle to return true.

    g.print_graph()
    print(bfs(g, 0))
    print(dfs(g, 0))
    print('are there cycles', find_cycle(g))

    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 2)
    print('find mother', find_mother(g))
    print('find mother', find_mother_kosaraju(g))

    g = Graph(4)
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 1)
    print('find mother', find_mother(g))
    print('find mother', find_mother_kosaraju(g))

    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    print('find mother', find_mother(g))
    print('find mother', find_mother_kosaraju(g))

    g = Graph(9, directed=False)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(5, 3)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    g.add_edge(6, 4)
    g.add_edge(7, 8)

    print('number of edges:', num_edges(g))

    g = Graph(9)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(5, 3)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    g.add_edge(6, 4)
    g.add_edge(7, 8)
    g.print_graph()

    print('is there a path between 0 to 8', check_path(g, 0, 8))


main()
