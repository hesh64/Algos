from collections import deque


# import time

def make_get_time():
    time = 0

    def get_time():
        nonlocal time
        time += 1
        return time

    return get_time


get_time = make_get_time()


class Graph:
    def __init__(self, vertices):
        self.size = vertices;
        self.vertices = {}

        for i in range(1, vertices + 1):
            self.vertices[i] = []

    def insert(self, s, d):
        self.vertices[s].append(d)

    def bfs(self, i):
        color = 'color'
        dist = 'dist'
        pred = 'pred'

        properties = {}
        s = None
        for k in self.vertices:
            if k == i:
                s = k
            properties[k] = {
                'color': 'w',
                'dist': -1,
                'pred': None
            }

        properties[s][color] = 'g'
        properties[s][dist] = 0
        properties[s][pred] = None

        if s is None:
            return

        que = deque()
        que.append(s)
        while que:
            u = que.popleft()
            for v in self.vertices[u]:
                if properties[v][color] == 'w':
                    properties[v][color] = 'g'
                    properties[v][dist] = properties[u][dist] + 1
                    properties[v][pred] = u
                    que.append(v)
            properties[u][color] = 'b'

        return properties

    def dfs(self):
        get_time = make_get_time()
        properties = {}
        star_time = 'start_time'
        end_time = 'end_time'
        color = 'color'
        pred = 'pred'

        def dfs_visit(u):
            properties[u][star_time] = get_time()
            properties[u][color] = 'g'
            for v in self.vertices[u]:
                if properties[v][color] == 'w':
                    properties[v][pred] = u
                    dfs_visit(v)

            properties[u][color] = 'b'
            properties[u][end_time] = get_time()

        for i in range(1, len(self.vertices) + 1):
            properties[i] = {}
            properties[i][color] = 'w'
            properties[i][pred] = None

        for i in range(1, len(self.vertices) + 1):
            if properties[i][color] == 'w':
                dfs_visit(i)

        return properties

    def find_scc(self):
        props = self.dfs()

        selft = Graph(self.size)
        for u in self.vertices:
            for v in self.vertices[u]:
                selft.insert(v, u)

        vertices = [k for k in selft.vertices.keys()]
        vertices.sort(key=lambda x: props[x]['end_time'], reverse=True)
        c, p = 'c', 'p'
        propst = {}
        for i in vertices:
            propst[i] = {}
            propst[i][c] = 'w'
            propst[i][p] = None

        def dfs(gt, ut, pt):
            pt[ut][c] = 'g'
            for vt in gt.vertices[ut]:
                if pt[vt][c] == 'w':
                    pt[vt][c] = 'grey'
                    pt[vt][p] = ut
                    dfs(gt, vt, pt)
            pt[ut][c] = 'b'

        for i in vertices:
            if propst[i][c] == 'w':
                dfs(selft, i, propst)

        for k in propst:
            if propst[k][p] is None:
                print(k, 'is a strongly connected component')

    def print_path(self, s, v, properties):
        if s == v:
            print(s)
        elif properties[v]['pred'] is None:
            return None
        else:
            self.print_path(s, properties[v]['pred'], properties)
            print(v)


def main():
    g = Graph(5)
    edges = [[1, 2], [1, 5], [5, 2], [2, 4], [5, 4], [2, 3], [4, 3]]
    for edge in edges:
        g.insert(edge[0], edge[1])

    for k in g.vertices:
        print(k, g.vertices[k])

    print('path')
    properties = g.bfs(1)
    g.print_path(1, 3, properties)

    print('\n\n\nbfs---')

    g = Graph(6)
    edges = [[1, 2], [1, 4], [4, 2], [2, 3], [3, 4], [5, 3], [5, 6], [6, 6]]

    for edge in edges:
        g.insert(edge[0], edge[1])

    for k in g.vertices:
        print(k, g.vertices[k])

    properties = g.dfs()
    for k in properties:
        print(k, properties[k])

    print('\n\nstrongly connected components')

    g = Graph(8)
    edges = [[1, 2], [2, 5], [5, 1], [2, 3],
             [3, 4], [4, 3], [2, 6], [5, 6],
             [6, 7], [7, 6], [4, 8], [8, 8]]

    for edge in edges:
        g.insert(edge[0], edge[1])

    g.find_scc()


main()
