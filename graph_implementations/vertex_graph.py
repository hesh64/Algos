from collections import deque


class Vertex:
    def __init__(self, x):
        self.x = x
        self.ins = set()
        self.outs = set()

    def add_in_edge(self, fedge):
        self.ins.add(fedge)

    def add_out_edge(self, oedge):
        self.outs.add(oedge)


class Graph:
    def __init__(self):
        self.sets = {}

    def add_edge(self, f, t):
        if f not in self.sets:
            self.sets[f] = Vertex(f)
        if t not in self.sets:
            self.sets[t] = Vertex(t)

        self.sets[f].add_out_edge(t)
        self.sets[t].add_in_edge(f)

    def remove_edge(self, f, t):
        self.sets[f].outs.remove(t)
        self.sets[t].ins.remove(f)

    def dfs(self, dir, s, pre=lambda x: None, post=lambda x: None):
        stack = [(s, False)]

        while stack:
            u, processed = stack.pop()

            if u and not processed:
                neighbors = self.sets[u].ins if dir == 'in' else self.sets[u].outs
                pre(self.sets[u])
                stack.append((u, True))
                stack.extend([(v, False) for v in neighbors])

            elif u and processed:
                post(self.sets[u])

    def bfs(self, dir, s, pre=lambda x: None, post=lambda x: None):
        d = deque([s, False])

        pre(self.sets[s])
        while d:
            n = len(d)
            for _ in range(n):
                u = d.popleft()
                neighbors = self.sets[u].ins if dir == 'in' else self.sets[u].outs
                post(u)
                for v in neighbors:
                    pre(self.sets[v])


g = Graph()
g.add_edge('a', 'b')
g.add_edge('b', 'c')
g.add_edge('c', 'd')
g.add_edge('e', 'c')


def pre(v):
    print(v.x)


g.dfs('in', 'c', pre)
