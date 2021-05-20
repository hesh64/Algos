def maze_has_path(m):
    max_row, max_col = len(m), len(m[0])
    path = []

    def helper(row, col):
        nonlocal max_row, max_col
        path.append((row, col))
        if 0 <= row < max_row and 0 <= col < max_col:
            if row == 0 and col == max_col - 1:
                return True

            m[row][col] = True

            if any(helper(row + r, col + c)
                   for r, c in [[1, 0], [-1, 0], [0, 1], [0, -1]] if 0 <= row + r < max_row and 0 <= col + c < max_col
                                                                     and m[row + r][col + c] == 0 and
                                                                     m[row + r][col + c] == 0):
                return path

            m[row][col] = False
            path.pop()
            return False

    return helper(max_row - 1, 0)


m = [
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
]

print(maze_has_path(m))

start = 5, 4
m = [
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
]

from collections import deque


def flip_dfs(m, start):
    color = m[start[0]][start[1]]

    que = deque()
    que.append(start)

    while que:
        row, col = que.popleft()
        m[row][col] = 1 if color == 0 else 1
        for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0 <= row + r < len(m) and 0 <= col + c < len(m[0]) and m[row + r][col + c] == color:
                que.append((row + r, col + c))

    return m


print('\n\nflip_dfs')
flip_dfs(m, start)

start = 5, 4
m = [
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
]
for r in m:
    print(r)


def flip_bfs(m, start):
    max_row, max_col = len(m), len(m[0])
    color = m[start[0]][start[1]]

    def helper(row, col):
        nonlocal max_row, max_col, color
        if not (0 <= row < max_row and 0 <= col < max_col):
            return

        m[row][col] = 1 if color == 0 else 1
        for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0 <= row + r < max_row and 0 <= col + c < max_col and m[row + r][col + c] == color:
                helper(row + r, col + c)

    helper(*start)


flip_bfs(m, start)
print('\n\nflip_bfs')
for r in m:
    print(r)

m = [
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]


def compute_enclosed_regions(m):
    no_visit = set()

    def dfs(row, col):
        no_visit.add((row, col))

        for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0 <= row + r < len(m) and 0 <= col + c < len(m[0]) \
                    and (row + r, col + c) not in no_visit and m[row + r][col + c] == 0:
                dfs(row + r, col + c)

    for i in range(len(m[0])):
        if m[0][i] == 0 and (0, i) not in no_visit:
            dfs(0, i)
        if m[len(m) - 1][i] == 0 and (len(m) - 1, i) not in no_visit:
            dfs(len(m) - 1, i)

    for i in range(len(m)):
        if m[i][0] == 0 and (i, 0) not in no_visit:
            dfs(i, 0)
        if m[i][len(m[0]) - 1] == 0 and (i, len(m[0]) - 1) not in no_visit:
            dfs(len(m[0]) - 1, i)

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0 and (i, j) not in no_visit:
                m[i][j] = 1

    return m


print('\n\ncompute_enclosed_regions')
compute_enclosed_regions(m)
for r in m:
    print(r)


class Graph:
    def __init__(self, n, edges):
        self.vertices = n
        self.edges = {i: [] for i in range(n)}
        for u, v in edges:
            self.edges[u].append(v)


def check_for_cycle(g):
    n = g.vertices
    stack = [False] * n

    def dfs(u, stack):
        if stack[u]:
            return True

        stack[u] = True
        if any(dfs(v, stack) for v in g.edges[u]):
            return True

        stack[u] = False

        return False

    return any(dfs(i, stack) for i in range(n))


def check_for_cycle2(graph):
    w, g, b = range(3)
    n = graph.vertices
    color = {i: w for i in range(n)}

    def dfs(u):
        nonlocal w, g, b
        if color[u] == g:
            return True

        color[u] = g
        if any(dfs(v) for v in graph.edges[u] if color[v] != b):
            return True

        color[u] = b
        return False

    return any(dfs(i) for i in range(n))


g = Graph(13,
          [[0, 1], [1, 4], [2, 3], [3, 4], [4, 5], [5, 6], [4, 7], [5, 8], [8, 12], [12, 10], [8, 9], [10, 11],
           [11, 8]])
print('\n\ncheck_for_cycles')
print(check_for_cycle(g))
print(check_for_cycle2(g))

g = Graph(13,
          [[0, 1], [1, 4], [2, 3], [3, 4], [4, 5], [5, 6], [4, 7], [5, 8], [8, 12], [12, 10], [8, 9], [10, 11]])
print('\n\ncheck_for_cycles')
print(check_for_cycle(g))
print(check_for_cycle2(g))


class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = []

    def to(self, v):
        self.edges.append(v)


class Graph:
    def __init__(self, n, edges):
        self.vertices = [None] * n

        for u, v in edges:
            if self.vertices[u] is None:
                self.vertices[u] = Vertex(u)

            if self.vertices[v] is None:
                self.vertices[v] = Vertex(v)

            self.vertices[u].to(self.vertices[v])

    def add(self, u):
        self.vertices[u.data] = u


g = Graph(13,
          [[0, 1], [1, 4], [2, 3], [3, 4], [4, 5], [5, 6], [4, 7], [5, 8], [8, 12], [12, 10], [8, 9], [10, 11]])


def clone(g):
    n = len(g.vertices)
    new_g = Graph(n, [])

    def dfs(s):
        if new_g.vertices[s.data] is None:
            new_g.vertices[s.data] = Vertex(s.data)
            new_g.vertices[s.data].edges = [dfs(u) for u in s.edges]

        return new_g.vertices[s.data]

    for v in g.vertices:
        dfs(v)
    return new_g


print('\n\nog')
for v in g.vertices:
    print(v.data, v.edges)

print('\nclone')
for v in clone(g).vertices:
    print(v.data, v.edges)


class Graph:
    def __init__(self, n, edges):
        self.vertices = n
        self.edges = {i: [] for i in range(n)}
        for u, v in edges:
            self.edges[u].append(v)


def bipartite_graph(g):
    colors = {}
    black, white = 1, 2

    def dfs(s, color):
        nonlocal black, white

        if s not in colors:
            colors[s] = color

        for u in g.edges[s]:
            if u in colors and colors[u] == color:
                return False
            elif u not in colors and dfs(u, black if color == white else white) is False:
                return False

        return True

    return dfs(0, black)


g = Graph(22, [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [4, 5], [3, 5], [1, 7], [7, 6], [3, 6], [6, 15], [7, 8], [8, 10],
               [10, 11], [11, 12], [12, 13], [13, 14], [14, 21], [11, 18], [9, 11], [9, 16], [6, 9], [15, 16],
               [16, 17], [17, 19], [18, 19], [19, 20], [20, 21]])

print('\n\nbipartied_graph')
print(bipartite_graph(g))

g = Graph(22, [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [4, 5], [3, 5], [1, 7], [7, 6], [3, 6], [6, 15], [7, 8], [8, 10],
               [10, 11], [11, 12], [12, 13], [13, 14], [14, 21], [11, 18], [9, 11], [9, 16], [6, 9], [15, 16],
               [16, 17], [17, 19], [18, 19], [19, 20], [20, 21], [19, 11]])

print(bipartite_graph(g))

from collections import deque

words = {'bat', 'cot', 'dog', 'dag', 'dot', 'cat'}


def transform_string(s, start, end):
    g, m = {}, {}
    n = len(start)
    q = deque()

    for word in words:
        m[word] = set()
        for i in range(n):
            w = word[:i] + '_' + word[i + 1:]
            if w not in g:
                g[w] = []
            g[w].append(word)
            m[word].add(w)

    q.append((start, tuple([start])))
    s.remove(start)

    while q:
        word, t = q.popleft()
        if word in s:
            s.remove(word)

        for mue in m[word]:
            for w in g[mue]:
                if w == end:
                    return t + tuple([w])

                if w in s:
                    q.append((w, t + tuple([w])))
    return -1


print(transform_string(words, 'cat', 'dog'))

import string
import collections

words = {'bat', 'cot', 'dog', 'dag', 'dot', 'cat'}


def trans_string(D, s, t):
    StringWithDistance = collections.namedtuple('StringWithDistance', ('candidate_string', 'distance'))
    q = deque([StringWithDistance(s, 0)])
    D.remove(s)

    while q:
        f = q.popleft()
        if f.candidate_string == t:
            return f.distance

        for i in range(len(f.candidate_string)):
            for c in string.ascii_lowercase:
                cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, f.distance + 1))

    return -1


print(trans_string(words, 'cat', 'dog'))
