from typing import List


def indel(c):
    """
        cost of an insert of delete
    """
    return 1


def match(c, b):
    """
    cost of matching or substituting

    """
    return 0 if c == b else 1


def string_compare_rec(s, t, i, j):
    if i == 0:
        return j * indel(' ')

    if j == 0:
        return i * indel(' ')

    opt = [None] * 3

    # match
    opt[0] = string_compare_rec(s, t, i - 1, j - 1) + match(s[i], t[j])
    # insert
    opt[1] = string_compare_rec(s, t, i, j - 1) + indel(t[j])
    # delete
    opt[2] = string_compare_rec(s, t, i - 1, j) + indel(s[i])

    return min(opt)


"""
if you run this it'll run too slow
"""

# s1 = 'lasasdfasfd'
# s2 = 'lagadfsdfsfsdfs'
# print(string_compare(s1, s2, len(s1), len(s2)))

MOVES = {
    0: 'M',
    1: 'I',
    2: 'D'
}

MATCH, INSERT, DELETE = range(3)


class Cell:
    def __init__(self, cost, parent=-1):
        self.cost, self.parent = cost, parent

    def __repr__(self):
        return f'({self.cost}, {MOVES[self.parent] if self.parent in MOVES else self.parent})'


def init_col(m, i, j):
    '''
    init col 0
    :param m:
    :return:
    '''
    m[i][0].cost = i
    m[i][0].parent = -1
    if i > 0:
        m[i][0].parent = DELETE
    else:
        m[i][0].parent = -1


def init_row(m, i, j):
    '''
    init row 0
    :param m:
    :return:
    '''
    m[0][j].cost = j
    if j > 0:
        m[0][j].parent = INSERT
    else:
        m[0][j].parent = -1


def process_result(s, t, m, i, j):
    # what to do with the result
    return m[i][j].cost, reconstruct_path(s, t, m, i, j)


"""
where wil the result be sitting
"""
goal_cell = lambda s, t: (len(s) - 1, len(t) - 1)


def string_compare(s, t, process_result, init_row, init_col, goal_cell):
    """
        notice the padding we are adding in order to make the indexing easier..
    """
    # Initializing
    s = ' ' + s
    t = ' ' + t

    max_len = max(len(s), len(t))
    m: List[List[Cell]] = [[Cell(0) for _ in range(max_len)] for _ in range(max_len)]

    # customizable initialization
    for j in range(max_len):
        init_col(m, 0, j)
    for i in range(max_len):
        init_row(m, i, 0)

    # business logic
    opts = [None] * 3

    for i in range(1, len(s)):
        for j in range(1, len(t)):
            opts[MATCH] = m[i - 1][j - 1].cost + match(s[i], t[j])
            opts[INSERT] = m[i][j - 1].cost + indel('')
            opts[DELETE] = m[i - 1][j].cost + indel('')

            m[i][j].cost, m[i][j].parent = opts[MATCH], MATCH
            for k in range(INSERT, DELETE + 1):
                if opts[k] < m[i][j].cost:
                    m[i][j].cost, m[i][j].parent = opts[k], k

    # where is the result sitting
    i, j = goal_cell(s, t)

    return process_result(s, t, m, i, j)


def reconstruct_path(s, t, m, i, j):
    if m[i][j].parent == -1:
        return ''

    if m[i][j].parent == MATCH:
        return reconstruct_path(s, t, m, i - 1, j - 1) + ('M' if s[i] == t[j] else 'S')

    if m[i][j].parent == INSERT:
        return reconstruct_path(s, t, m, i, j - 1) + 'I'

    if m[i][j].parent == DELETE:
        return reconstruct_path(s, t, m, i - 1, j) + 'D'


print(string_compare('salim', 'aalin', process_result=process_result, init_row=init_row, init_col=init_col,
                     goal_cell=goal_cell))
