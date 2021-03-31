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
            parent_level = 0
            if i in in_degrees:
                parent_level = in_degrees[i]
            in_degrees[v.vertex] += parent_level + 1
            v = v.next

    count = 0
    for k, v in in_degrees.items():
        if v + 1 == level:
            count += 1

    return count


if __name__ == "__main__":
    V = 5  # Total vertices
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(number_of_nodes(g, 3))
