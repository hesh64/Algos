def backtrack(a, k, input,
              is_a_solution=lambda *a: True,
              process_solution=lambda *a: None,
              construct_candidates=lambda *a: ([], 0),
              make_move=lambda *a: None,
              unmake_move=lambda *a: None
              ):
    finished = False

    def helper(a, k, input):
        """

        :param a: a partial solution
        :param k: first k elements
        :param input: the data we are processing
        :return:
        """
        if is_a_solution(a, k, input):
            process_solution(a, k, input)
        else:
            k += 1

            # c, ncandidates = construct_candidates(a, k, input, c, ncandidates)
            c, ncandidates = construct_candidates(a, k, input)

            for i in range(ncandidates):
                a[k] = c[i]

                make_move(a, k, input)
                helper(a, k, input)
                unmake_move(a, k, input)

                if finished:
                    return

    helper(a, k, input)


def all_subsets_of_n(n):
    subsets = []

    def is_a_solution(a, k, input):
        return k == input

    def process_solution(a, k, input):
        subsets.append([i for i in range(n + 1) if a[i]])

    def construct_candidates(a, k, input):
        return [True, False], 2

    backtrack([None] * (n + 1), 0, n,
              is_a_solution=is_a_solution,
              process_solution=process_solution,
              construct_candidates=construct_candidates,
              )
    return subsets


print(all_subsets_of_n(4))


def all_permutations_of_n(n):
    perms = []

    def is_a_solution(a, k, input):
        return k == n

    def process_solution(a, k, input):
        perms.append(a[1:])

    def construct_candidates(a, k, input):
        in_perm = [False] * (input + 1)
        for i in range(1, k):
            in_perm[a[i]] = True

        p = [i for i in range(1, input + 1) if in_perm[i] is False]
        return p, len(p)

    backtrack([0] * (n + 1), 0, n,
              is_a_solution=is_a_solution,
              process_solution=process_solution,
              construct_candidates=construct_candidates,
              )
    return len(perms), perms


print(all_permutations_of_n(5))


class Graph:
    def __init__(self, n):
        self.nvertices = n
        self.edges = {i: set() for i in range(1, n + 1)}

    def add_edge(self, u, v):
        self.edges[u].add(v)
        self.edges[v].add(u)


from collections import namedtuple

GraphForPath = namedtuple('GraphForPath', ('s', 't', 'g'))


def all_paths_in_a_graph(input):
    paths = 0

    def is_a_solution(a, k, input):
        return a[k] == input.t

    def process_solution(a, k, input):
        nonlocal paths
        paths += 1
        print('process_solution', a[:k + 1])

    def construct_candidates(a, k, input):
        in_path = [False] * (input.g.nvertices + 1)

        for i in range(1, k):
            in_path[a[i]] = True

        c = [None] * (input.g.nvertices + 1)
        ncandidates = 0

        if k == 1:
            c[0] = input.s
            return c, 1

        last = a[k - 1]
        for p in input.g.edges[last]:
            if in_path[p] is False:
                c[ncandidates] = p
                ncandidates += 1

        return c, ncandidates

    a = [None] * (input.g.nvertices + 1)
    backtrack(a, 0, input,
              is_a_solution=is_a_solution,
              process_solution=process_solution,
              construct_candidates=construct_candidates,
              )

    return paths


g = Graph(6)
for u, v in [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 6], [4, 6], [5, 6], [3, 4]]:
    g.add_edge(u, v)

paths = all_paths_in_a_graph(GraphForPath(1, 3, g))
print(paths)
