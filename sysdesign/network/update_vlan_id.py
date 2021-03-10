# O(n)
def update_ids(m, start, old_id, new_id):
    visited = [[False for i in range(len(m[0]))] for j in range(len(m))]

    def dfs(matrix, pos, visited, old_id, new_id):
        row, col = pos
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) \
                and visited[row][col] is False and matrix[row][col] == old_id:
            visited[row][col] = True
            dfs(matrix, (row + 1, col), visited, old_id, new_id)
            dfs(matrix, (row - 1, col), visited, old_id, new_id)
            dfs(matrix, (row, col + 1), visited, old_id, new_id)
            dfs(matrix, (row, col - 1), visited, old_id, new_id)
            matrix[row][col] = 2

    dfs(m, start, visited, old_id, new_id)


def main():
    matrix = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 1],
    ]
    update_ids(matrix, (2, 2), 1, 2)
    for row in matrix:
        print(row)


main()
