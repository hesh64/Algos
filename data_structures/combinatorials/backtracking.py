def backtrack(a, k, input,
              is_a_solution=lambda *a: None,
              process_solution=lambda *a: None,
              construct_candidates=lambda *a: (None, None),
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
        return k == n

    def process_solution(a, k, input):
        subsets.append([i for i in range(n + 1) if a[i]])

    def construct_candidates(a, k, input):
        return [True, False], 2

    backtrack([None] * (n + 1), 0, 3,
              is_a_solution=is_a_solution,
              process_solution=process_solution,
              construct_candidates=construct_candidates,
              )
    return subsets


print(all_subsets_of_n(21))
