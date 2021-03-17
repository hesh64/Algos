class vertex:
    def __init__(self, id, visited):
        self.id = id
        # Boolean
        self.visited = visited


class edge:
    def __init__(self, weight, visited, src, dest):
        self.weight = weight
        # Boolean
        self.visited = visited
        self.src = src
        self.dest = dest


class Graph:
    def __init__(self, v, e):
        self.input_v = v
        self.input_e = e
        self.vertices = []
        self.edges = []

    def vertex_exists(self, id):
        for i in range(len(self.vertices)):
            if self.vertices[i].id == id:
                return self.vertices[i]
        return None

    def generate_graph(self):
        for i in range(1, self.input_v + 1):
            vert = vertex(i, False)
            self.vertices.append(vert)
        print([v.id for v in self.vertices])

        for cost, source, dest in self.input_e:
            src = self.vertex_exists(source)
            dest = self.vertex_exists(dest)
            print(source, src, dest)
            e = edge(cost, False, src, dest)
            self.edges.append(e)

    def find_min_spanning_tree(self):
        weight = 0
        vertices = 1

        head = self.vertices[0]
        head.visited = True
        vertices += 1

        while vertices < len(self.vertices):
            smallest = None
            # find an edge no one touched ever before
            for i in range(len(self.edges)):
                if self.edges[i].visited == False and self.edges[i].dest.visited == False:
                    smallest = self.edges[i]
                    break
            # find an edge whos source we've visited but
            # not destination, and who's weight is less.
            for i in range(len(self.edges)):
                if self.edges[i].visited == False:
                    if self.edges[i].src.visited == True and self.edges[i].dest.visited == False:
                        if smallest is None or smallest.weight > self.edges[i].weight:
                            smallest = self.edges[i]

            smallest.visited = True
            smallest.dest.visited = True
            weight += smallest.weight
            vertices += 1

        return weight


def main():
    v = 7
    e = [[2, 1, 4], [1, 1, 3], [2, 1, 2],
         [1, 3, 4], [3, 2, 4], [2, 3, 5],
         [2, 4, 7], [1, 5, 6], [2, 5, 7]]

    g = Graph(v, e)
    g.generate_graph()
    mst = g.find_min_spanning_tree()
    print(mst)


main()
