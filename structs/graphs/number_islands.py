"""
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

"""


def count_islands(m):
    visited = [[False for _ in range(len(m[0]))] for _ in range(len(m))]

    def dfs(_m, x, y, _visited):
        if x < 0 or x >= len(_m) or y >= len(_m[0]) or y < 0 or _m[x][y] == '0':
            return

        if _visited[x][y]:
            return

        _visited[x][y] = True

        dfs(_m, x - 1, y, _visited)
        dfs(_m, x + 1, y, _visited)
        dfs(_m, x, y + 1, _visited)
        dfs(_m, x, y - 1, _visited)

    count = 0
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col] == '1' and visited[row][col] is False:
                dfs(m, row, col, visited)
                count += 1

    return count


"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) You may assume all 
four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum
area is 0.)

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
"""


# O(V^2)
def largest_islands(m):
    visited = [[False for _ in range(len(m[0]))] for _ in range(len(m))]

    def dfs(_m, x, y, _visited):
        if x < 0 or x >= len(_m) or y >= len(_m[0]) or y < 0 or _m[x][y] == 0:
            return 0

        if _visited[x][y]:
            return 0

        _visited[x][y] = True

        return 1 + dfs(_m, x - 1, y, _visited) + dfs(_m, x + 1, y, _visited) + dfs(_m, x, y + 1, _visited) + dfs(_m, x,
                                                                                                                 y - 1,
                                                                                                                 _visited)

    size = 0
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col] == 1 and visited[row][col] is False:
                isize = dfs(m, row, col, visited)
                size = max(size, isize)

    return size


"""
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where 
"adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be
used more than once.

"""


# todo needs a tad more work, we need to back track!
def exists(m, word):
    def dfs(_m, x, y, _visited, word, idx=0):
        if idx >= len(word):
            return True

        if x < 0 or x >= len(_m) or y >= len(_m[0]) or y < 0 or _m[x][y] != word[idx]:
            return False

        if _visited[x][y]:
            return False

        _visited[x][y] = True

        found = False
        if dfs(_m, x - 1, y, _visited, word, idx + 1):
            found = True

        elif dfs(_m, x + 1, y, _visited, word, idx + 1):
            found = True

        elif dfs(_m, x, y + 1, _visited, word, idx + 1):
            found = True
        elif dfs(_m, x, y - 1, _visited, word, idx + 1):
            found = True

        if found is False:
            _visited[x][y] = False
            return False

        return True

    for row in range(len(m)):
        for col in range(len(m[0])):
            visited = [[False for _ in range(len(m[0]))] for _ in range(len(m))]
            if m[row][col] == word[0]:
                if dfs(m, row, col, visited, word):
                    return True

    return False


def main():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    result = count_islands(grid)
    print(f'there are {result} islans')
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result = count_islands(grid)
    print(f'there are {result} islans')
    grid = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ]
    result = count_islands(grid)
    print(f'there are {result} islans')

    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    result = largest_islands(grid)
    print(f'the largest island {result}')

    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"
    result = exists(board, word)
    print(f'does {word} exists? {result}')

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    result = exists(board, word)
    print(f'does {word} exists? {result}')

    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCB"
    result = exists(board, word)
    print(f'does {word} exists? {result}')


main()
