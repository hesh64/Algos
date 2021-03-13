def low_coverage_area(matrix):
    max_count = 0

    def check(matrix, start, end, row):
        nonlocal max_count
        count = 0
        for i in range(row, len(matrix)):
            temp = 0
            for j in range(start, end):
                if matrix[i][j] == 1:
                    temp += 1
                else:
                    max_count = max(max_count, count)
                    return
            count += temp

    for row in range(len(matrix)):
        col = 0
        while col < len(matrix[0]):
            if matrix[row][col] == 1:
                start = col
                end = col + 1
                while col < len(matrix[0]) and matrix[row][end] == matrix[row][end - 1]:
                    col += 1
                check(matrix, start, col, row)

            col += 1

    return max_count


def main():
    matrix = [
        [0, 1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 1],
        [0, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0]
    ]

    print(low_coverage_area(matrix))
    matrix = [[1, 0, 1, 0, 0],
              [1, 0, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 0, 0, 1, 0]]

    print(low_coverage_area(matrix))


main()
