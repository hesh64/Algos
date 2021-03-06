"""helpers"""


class Node:
    def __init__(self, d):
        self.data = d
        self.friends = []


from random import shuffle


# this is un-directed graph i.e.
# if there is an edge from x to y
# that means there must be an edge from y to x
# and there is no edge from a node to itself
# hence there can maximim of (nodes * nodes - nodes) / 2 edgesin this graph
def create_test_graph_directed(nodes_count, edges_count):
    vertices = []
    for i in range(0, nodes_count):
        vertices += [Node(i)]

    all_edges = []
    for i in range(0, nodes_count):
        for j in range(i + 1, nodes_count):
            all_edges.append([i, j])

    shuffle(all_edges)

    for i in range(0, min(edges_count, len(all_edges))):
        edge = all_edges[i]
        vertices[edge[0]].friends += [vertices[edge[1]]]
        vertices[edge[1]].friends += [vertices[edge[0]]]

    return vertices


def print_graph(vertices):
    for n in vertices:
        print(str(n.data), end=": {")
        for t in n.friends:
            print(str(t.data), end=" ")
        print()


def print_graph_rec(root, visited_nodes):
    if root == None or root in visited_nodes:
        return

    visited_nodes.add(root)

    print(str(root.data), end=": {")
    for n in root.friends:
        print(str(n.data), end=" ")
    print("}")

    for n in root.friends:
        print_graph_rec(n, visited_nodes)


def print_graph(root):
    visited_nodes = set()
    print_graph_rec(root, visited_nodes)


"""end"""

"""clone graph"""


def clone(node):
    completed = {}
    return clone_rec(node, completed)


def clone_rec(node, comp):
    if node is None:
        return None

    new_node = Node(node.data)
    comp[new_node.data] = new_node
    for friend in node.friends:
        if friend.data not in comp:
            clone_rec(friend, comp)
        new_node.friends.append(comp[friend.data])

    return new_node


def main():
    vertices = create_test_graph_directed(7, 18)
    print_graph(vertices[0])
    print('---')
    cp = clone(vertices[0])
    print_graph(cp)


main()
