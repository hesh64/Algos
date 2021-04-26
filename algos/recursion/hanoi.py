def move_n_rings(n):
    moves = []
    f_peg, t_peg, u_peg = 0, 1, 2
    pegs = [[] for i in range(3)]
    pegs[f_peg] = [1 + i for i in range(n)]

    def move_rings(n_to_move, fr, to, us):
        nonlocal moves, pegs

        if n_to_move > 0:
            move_rings(n_to_move - 1, fr, us, to)
            pegs[to].append(pegs[fr].pop())
            moves.append([fr, to])
            move_rings(n_to_move - 1, us, to, fr)

    move_rings(n, f_peg, t_peg, u_peg)
    return moves


def main():
    n = 3
    print(move_n_rings(n))


main()
