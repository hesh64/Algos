def is_split_possible(graph):
    color = {}

    def dfs(g, p, color):
        for i in g[p]:
            if i in color:
                if color[i] == color[p]:
                    return False
            else:
                color[i] = 1 - color[p]
                if not dfs(g, p, color):
                    return False
        return True

    for i in range(len(graph)):
        if i not in color:
            color[i] = 0
            if not dfs(graph, i, color):
                return False
    return True


def main():
    # Driver code
    graph = [[3], [2, 4], [1], [0, 4], [1, 3]]
    print(is_split_possible(graph))


main()
