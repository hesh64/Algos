import heapq


class Graph:
    def __init__(self, n, edges):
        self.size = n
        self.vertices = {}
        for i in range(1, n + 1):
            self.vertices[i] = []

        self.weights = {}

        for s, d, w in edges:
            self.vertices[s].append(d)
            self.weights[(s, d)] = w

    def get_weight(self, s, d):
        return self.weights[(s, d)]

    def insert(self, s, d, w):
        self.vertices[s].append(d)
        self.weights[(s, d)] = w


def init_graph(g, s):
    properties = {}
    for i in range(1, g.size + 1):
        properties[i] = {
            'd': float('inf'),
            'p': None
        }

    properties[s]['d'] = 0
    return properties


def relax(gp, u, v, w):
    if gp[v]['d'] > gp[u]['d'] + w:
        gp[v]['d'] = gp[u]['d'] + w
        gp[v]['p'] = u


# O(V * E)
def bellman_ford(g: Graph, s: int):
    # O(V)
    gp = init_graph(g, s)

    # O((V - 1) * E)
    for _ in range(g.size - 1):
        for u in g.vertices:
            for v in g.vertices[u]:
                relax(gp, u, v, g.get_weight(u, v))

    # O(E)
    for u in g.vertices:
        for v in g.vertices[u]:
            # if get_wight is negative this condition will be true
            # and the cycle is detected.
            if gp[v]['d'] > gp[u]['d'] + g.get_weight(u, v):
                return False

    return True


def topological_sort(g: Graph):
    in_degrees = {i: 0 for i in range(1, g.size + 1)}
    for u in g.vertices:
        for v in g.vertices[u]:
            in_degrees[v] += 1

    # print(in_degrees)

    mothers = []
    for k in in_degrees:
        if in_degrees[k] == 0:
            mothers.append(k)

    ordered = []
    while mothers:
        u = mothers.pop(0)
        ordered.append(u)

        for v in g.vertices[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                mothers.append(v)

    return ordered


# O(V + E)
def shortest_paths_in_dag(g: Graph, s):
    ordered = topological_sort(g)
    gp = init_graph(g, s)
    for u in ordered:
        for v in g.vertices[u]:
            relax(gp, u, v, g.get_weight(u, v))

    return [[v['p'], k, v['d']] for k, v in gp.items() if v['p'] is not None]


class Vertex:
    def __init__(self, index, d=float('inf'), p=None):
        self.index = index
        self.d = d
        self.p = p

    def __lt__(self, other):
        return self.d < other.d

    def __repr__(self):
        return f'({self.p}, {self.index}): {self.d}'


class HeapItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return f'({self.key}, {self.value})'


# This is an attempt to create a heap that will also maintain indices such that key_decrease operations
# will cost lg(v). I am too tired to implement the logic to deal with the inf values everywhere..
# But one I shall return to this.
class DijHeap:
    def __init__(self, key=lambda x: x):
        self.heap: [HeapItem] = []
        self.key_index = {}
        self.get_key = key

    def push(self, item):
        heapitem = HeapItem(self.get_key(item), item)
        index = len(self.heap)
        self.heap.append(heapitem)
        if heapitem.key != float('inf'):
            self.key_index[heapitem.key] = index

    def pop(self):
        key0, keym1 = self.heap[0].key, self.heap[-1].key
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        if self.heap[0].key != float('inf') and self.heap[-1].key != float('inf'):
            self.key_index[key0], self.key_index[keym1] = self.key_index[keym1], self.key_index[key0]
            del self.key_index[key0]

        item0 = self.heap.pop()
        self.siftdown(0)
        return item0.value

    def siftup(self, pos):
        parent = (pos - 1) // 2
        while parent >= 0 and pos < len(self.heap) and self.heap[pos].key < self.heap[parent].key:
            self.heap[pos], self.heap[parent] = self.heap[parent], self.heap[pos]
            self.key_index[pos], self.key_index[parent] = self.key_index[parent], self.key_index[pos]

        return parent

    def siftdown(self, pos):
        left, right = pos * 2 + 1, pos * 2 + 2

        if left < len(self.heap) and self.heap[pos].key < self.heap[left].key:
            self.heap[pos], self.heap[left] = self.heap[left], self.heap[pos]
            print(self.key_index)
            self.key_index[pos], self.key_index[left] = self.key_index[left], self.key_index[pos]

            return self.siftdown(left)
        elif right < len(self.heap) and self.heap[pos].key < self.heap[right].key:
            self.heap[pos], self.heap[right] = self.heap[right], self.heap[pos]
            self.key_index[pos], self.key_index[right] = self.key_index[right], self.key_index[pos]

            return self.siftdown(right)

        return pos

    def __repr__(self):
        return ','.join([str(i) for i in self.heap])

    def decrease_key(self, key, new_key):
        pos = self.key_index[key]
        self.key_index[new_key] = pos

        old_key = self.heap[pos].key
        self.heap[pos].key = new_key

        del self.key_index[key]
        new_pos = self.siftup(pos)
        self.key_index[old_key] = new_pos


def dijkstra_init_graph(g, s):
    properties = {}
    for i in range(1, g.size + 1):
        properties[i] = Vertex(i)

    properties[s].d = 0
    print(properties)
    return properties


def dijkstra_relax(u, v, w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.p = u.index


# O((V + E) lg V) remember that O(V) and O(E) are combined into O(V + E) because this is aggregated analysis
def dijkstra(g: Graph, s):
    vertices = dijkstra_init_graph(g, s)
    heap = []
    [heapq.heappush(heap, u) for _, u in vertices.items()]

    s = set()
    # V iterations O(V)
    while heap:
        u = heapq.heappop(heap)

        s.add(u)
        # E iterations O(E)
        for v in g.vertices[u.index]:
            dijkstra_relax(u, vertices[v], g.get_weight(u.index, v))
            # the heap implementation that we choose plays a key role
            # in the complexity of this algorithm
            # a standard heap will require v lg v to heapify with every operation,
            # key decrease operation would cost lg v, if you are able to find the key
            # in O(1) by maintaining an index map you save a full O(V) off by moving
            # from heapify to siftup from that pos.
            # we'll assume that we did that, so let's call this op O(lg v)
            heapq.heapify(heap)

    return s


def main():
    edges = [[1, 2, 6], [1, 5, 7], [2, 3, 5], [2, 5, 8], [2, 4, -4], [3, 2, -2], [4, 1, 2], [4, 3, 7], [5, 4, 9],
             [5, 3, -3]]

    g = Graph(5, edges)
    shortest = bellman_ford(g, 1)
    print(shortest)

    # 6 verts
    edges = [[1, 2, 5], [1, 3, 3], [2, 3, 2], [2, 4, 6], [3, 4, 7], [3, 5, 4], [3, 6, 2], [4, 5, -1], [4, 6, 1],
             [5, 6, -2]]
    g = Graph(6, edges)
    shortest = shortest_paths_in_dag(g, 2)
    print(shortest)

    print('\ndijkstra')
    edges = [[1, 2, 10], [1, 4, 5], [2, 3, 1], [2, 4, 2], [3, 5, 4], [5, 3, 6], [5, 1, 7], [4, 5, 2], [4, 2, 3],
             [4, 3, 9]]
    map = {1: 's', 2: 't', 3: 'x', 4: 'y', 5: 'z'}
    g = Graph(5, edges)
    shortest = dijkstra(g, 1)
    print(shortest)
    # print([[map[u.index], map[v.ind], w] for u, v, w in shortest])


main()
