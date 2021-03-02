"""
Minimum Height Trees (hard) #
We are given an undirected graph that has characteristics of a k-ary tree.
In such a graph, we can choose any node as the root to make a k-ary tree. The
root (or the tree) with the minimum height will be called Minimum Height Tree (MHT).
There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs.
Write a method to find all MHTs of the given graph and return a list of their roots.

Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
Output:[1, 2]
Explanation: Choosing '1' or '2' as roots give us MHTs. In the below diagram, we can see that the
height of the trees with roots '1' or '2' is three which is minimum.


Input: vertices: 4, Edges: [[0, 1], [0, 2], [2, 3]]
Output:[0, 2]
Explanation: Choosing '0' or '2' as roots give us MHTs. In the below diagram, we can see that the
height of the trees with roots '0' or '2' is three which is minimum.
"""

from collections import deque
from heapq import *


def find_trees(nodes, edges):
    graph = {i: [] for i in range(nodes)}
    for p, c in edges:
        graph[p].append(c)
        graph[c].append(p)

    minheap = []
    for i in range(nodes):
        visited = [False] * nodes
        mh = dfs_mh(graph, i, visited)
        heappush(minheap, (mh, i))

    top = minheap[0][0]
    mins = []
    while minheap[0][0] == top:
        mins.append(heappop(minheap)[1])
    return mins


def dfs_mh(graph, vertex, visited):
    if visited[vertex]:
        return 0
    visited[vertex] = True
    ch = 0
    for child in graph[vertex]:
        ch = max(dfs_mh(graph, child, visited), ch)

    visited[vertex] = False
    return 1 + ch


def find_mhtrees(vertices, edges):
    if vertices <= 0:
        return []

    if vertices == 1:
        return [0]

    in_degrees = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for p, c in edges:
        in_degrees[p] += 1
        in_degrees[c] += 1

        graph[p].append(c)
        graph[c].append(p)

    leaves = deque()
    for k in in_degrees:
        if in_degrees[k] == k:
            leaves.append(k)

    total_nodes = vertices
    while total_nodes > 2:
        leave_size = len(leaves)
        total_nodes -= leave_size
        for _ in range(leave_size):
            vertex = leaves.popleft()
            for child in graph[vertex]:
                in_degrees[child] -= 1
                if in_degrees[child] == 1:
                    leaves.append(child)

    return list(leaves)


def main():
    print("Roots of MHTs: " +
          str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[0, 1], [1, 2], [1, 3]])))


main()
