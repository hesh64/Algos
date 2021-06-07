def backtrack(a, k, input,
              is_a_solution=lambda *a: True,
              process_solution=lambda *a: None,
              construct_candidates=lambda *a: ([], 0),
              make_move=lambda *a: None,
              unmake_move=lambda *a: None
              ):
    finished = False

    def helper(a, k, input):
        nonlocal finished
        """

        :param a: a partial solution
        :param k: first k elements
        :param input: the data we are processing
        :return:
        """
        if is_a_solution(a, k, input):
            if process_solution(a, k, input):
                finished = True
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
    paths = []

    def is_a_solution(a, k, input):
        return a[k] == input.t

    def process_solution(a, k, input):
        paths.append(a[:k + 1])

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

    return len(paths), paths


g = Graph(6)
for u, v in [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 6], [4, 6], [5, 6], [3, 4]]:
    g.add_edge(u, v)

paths = all_paths_in_a_graph(GraphForPath(1, 3, g))
print(paths)

print('\n\n')
Point = namedtuple('Point', ('x', 'y'))


class Board:
    def __init__(self, prepopulate):
        self.m = [[None for _ in range(10)] for _ in range(10)]
        self.freecount = 9 * 9
        self.move = [None] * ((9 * 9) + 1)

        for x, y, v in prepopulate:
            self.m[x][y] = v
            self.freecount -= 1

    def p(self):
        print(''.join(['-' for _ in range(56)]))

        j = 0
        for r in self.m[1:]:
            i = 1
            for v in r[1:]:
                print(str(v).ljust(4), end=' | ' if i % 3 == 0 else ', ')
                i += 1
            j += 1
            print()
            if j % 3 == 0:
                print(''.join(['-' for _ in range(56)]))


import random

random.seed(42)


def solve_sudoku(b):
    def next_square(b):
        p = (random.randint(1, 9), random.randint(1, 9))
        while b.m[p[0]][p[1]] is not None:
            p = (random.randint(1, 9), random.randint(1, 9))
        return p

    def possible_next_moves(x, y, b):
        available = set([i for i in range(1, 10)])

        for i in range(1, 10):
            if b.m[i][y] is not None and b.m[i][y] in available:
                available.remove(b.m[i][y])

        for j in range(1, 10):
            if b.m[x][j] is not None and b.m[x][j] in available:
                available.remove(b.m[x][j])

        return list(available)

    def is_a_solution(a, k, b):
        return b.freecount == 0

    def process_solution(a, k, b):
        b.p()
        return True

    def construct_candidates(a, k, b):
        x, y = next_square(b)

        b.move[k] = Point(x, y)

        next_move_candidates = possible_next_moves(x, y, b)

        return next_move_candidates, len(next_move_candidates)

    def make_move(a, k, b):
        x, y = b.move[k]
        b.m[x][y] = a[k]
        b.freecount -= 1

    def unmake_move(a, k, b):
        x, y = b.move[k]
        b.m[x][y] = None
        b.freecount += 1

    backtrack([None] * (9 ** 2 + 1), 0, b,
              is_a_solution=is_a_solution,
              process_solution=process_solution,
              construct_candidates=construct_candidates,
              make_move=make_move,
              unmake_move=unmake_move
              )


b = Board([[1, 8, 1], [1, 9, 2], [2, 5, 3], [2, 6, 5],
           [3, 4, 6], [3, 8, 7], [4, 1, 7], [4, 7, 3], [5, 4, 4], [5, 7, 8],
           # [6, 1, 1], [7, 4, 1], [7, 5, 2], [8, 2, 8], [8, 8, 4], [9, 2, 5],
           [9, 7, 6], [1, 1, 6], [2, 1, 9], [3, 1, 8], [5, 1, 5], [7, 1, 4],
           # [1, 2, 7], [1, 3, 3], [1, 4, 8], [1, 5, 9], [1, 6, 4], [2, 2, 1],
           [2, 3, 2], [2, 4, 7], [2, 7, 4], [2, 9, 6], [9, 9, 8], [9, 1, 3],
           [9, 4, 9], [9, 5, 4], [6, 2, 3], [6, 3, 4], [6, 4, 5], [6, 5, 8],
           # [6, 6, 9], [6, 7, 2], [6, 8, 6], [6, 9, 7], [4, 2, 9], [4, 3, 8],
           [4, 4, 2], [4, 5, 6], [8, 1, 2], [8, 3, 7], [8, 4, 3], [8, 5, 5],
           [8, 6, 6], [8, 7, 1], [8, 8, 4], [8, 9, 9], [7, 7, 7], [7, 8, 3],
           [7, 9, 5], [4, 8, 5], [3, 2, 4], [3, 3, 5]],
          )
print(b.freecount)
b.p()
print(solve_sudoku(b))
