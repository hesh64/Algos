class AdjMatrix:
    def __init__(self, n):
        self.nvertices = n
        self.weight = [[float('inf') for _ in range(n)] for _ in range(n)]

    def add_edge(self, s, t, w):
        self.weight[s][t] = w
        self.weight[t][s] = w

    def __repr__(self):
        rows = []
        rows.append('    ' + ''.join([str(i).ljust(4, ' ') for i in range(g.nvertices)]))
        for i, row in enumerate(self.weight):
            rows.append((str(i) + ':').ljust(4, ' ') + ','.join([str(v).ljust(3, ' ') for v in row]))
        return '\n'.join(rows)


# On^3
def floyd(g: AdjMatrix):
    # if you add a parents matrix we can reconstruct the path!
    # but most all pairs distance applications don't need the path
    # define none edges with inf, that way you'll never select an non existing edge.
    for k in range(g.nvertices):
        for i in range(g.nvertices):
            for j in range(g.nvertices):
                g.weight[i][j] = min(g.weight[i][j], g.weight[i][k] + g.weight[k][j])
                # through_k = g.weight[i][k] + g.weight[k][j]
                # if through_k < g.weight[i][j]:
                #     g.weight[i][j] = through_k


g = AdjMatrix(6)
print(g)
for s, t, w in [[0, 1, 2], [0, 5, 6], [0, 4, 2, ], [0, 3, 5], [0, 2, 3], [1, 5, 1], [1, 2, 4], [2, 5, 3], [2, 3, 2],
                [3, 5, 1], [3, 4, 6], [4, 5, 7]]:
    g.add_edge(s, t, w)
print('-')
print(g)
print('-')
floyd(g)
print(g)
