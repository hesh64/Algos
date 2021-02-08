from collections import deque
from graph import Graph


# O(V + E)
# O(E)
def bfs_traversal(g, source):
    visited = {}
    result = ''
    q = deque()
    q.append(source)
    visited[source] = True

    while q:
        cur_node = q.popleft()
        result += str(cur_node)

        temp = g.array[cur_node].get_head()

        while temp:
            if temp.data not in visited:
                q.append(temp.data)
                visited[temp.data] = True
            temp = temp.next_element

    return result


g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(1, 5)
# g.add_edge(, 3)
# g.print_graph()
print(bfs_traversal(g, 0))
