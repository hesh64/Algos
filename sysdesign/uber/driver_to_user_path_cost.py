def get_total_cost(g_map, path_costs, drivers, user):
    #  generate the graph
    city = {}
    for point, cost in zip(g_map, path_costs):
        v1, v2 = point
        if v1 not in city:
            city[v1] = {}

        if v2 not in city:
            city[v2] = {}

        city[v1][v2] = cost
        city[v2][v1] = cost

    def dfs(graph, source, dist, visited):
        visited.add(source)
        ret = -1
        if dist in graph[source]:
            ret = graph[source][dist]

        else:
            for k in graph[source]:
                ret = graph[source][k] + dfs(graph, k, dist, visited)
                if ret != -1:
                    break

        visited.remove(source)
        return ret

    result = []
    for d in drivers:
        if d not in city:
            result.append(-1)
        else:
            visited = set()
            result.append(dfs(city, d, user, visited))

    return result


def main():
    G_map = [["a", "b"], ["b", "c"], ["a", "e"], ["d", "e"]]
    path_costs = [12.0, 23.0, 26.0, 18.0]
    drivers = ["c", "d", "e", "f"]
    user = "a"
    all_path_costs = get_total_cost(G_map, path_costs, drivers, user)
    print("Total cost of all paths", all_path_costs)


main()
