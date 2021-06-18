from collections import defaultdict, deque


def alienOrder(words) -> str:
    indeg = {c: 0 for c in ''.join(words)}
    g = defaultdict(set)

    for w1, w2 in zip(words, words[1:]):
        for u, v in zip(w1, w2):
            if u != v:
                if v not in g[u]:
                    g[u].add(v)
                    indeg[v] += 1
                break
        else:
            if len(w2) < len(w1):
                return ''

    queue = deque([u for u in indeg if indeg[u] == 0])
    order = ''
    while queue:
        u = queue.popleft()

        order += u

        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)

    if len(order) != len(indeg):
        return ''

    return order


print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
