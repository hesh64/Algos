def maximum_router(m):
    dp = [[0 for i in range(len(m[0]))] for j in range(len(m))]

    def dfs(matrix, p, dp):
        row, col = p
        cur = matrix[row][col]
        path = 0
        if dp[row][col] == 0:
            if row + 1 < len(matrix) and matrix[row + 1][col] > cur:
                path = max(path, dfs(matrix, (row + 1, col), dp))

            if row - 1 >= 0 and matrix[row - 1][col] > cur:
                path = max(path, dfs(matrix, (row - 1, col), dp))

            if col + 1 < len(matrix[0]) and matrix[row][col + 1] > cur:
                path = max(path, dfs(matrix, (row, col + 1), dp))

            if col - 1 >= 0 and matrix[row][col - 1] > cur:
                path = max(path, dfs(matrix, (row, col - 1), dp))

            dp[row][col] = path + 1
        return dp[row][col]

    max_num = 0
    for row in range(len(m)):
        for col in range(len(m[0])):
            max_num = max(max_num, dfs(m, (row, col), dp))

    return max_num


def main():
    matrix = [
        [2, 9, 6],
        [8, 4, 7],
        [5, 3, 1]
    ]

    print(maximum_router(matrix))


main()
