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


if __name__ == "__main__":
    V = 5  # Total vertices
    g = Graph(V)
    g.add_edge(1, 0)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)

    print(number_of_nodes(g, 1))
