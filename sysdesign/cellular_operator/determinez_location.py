def determine_location(matrix, loss_value):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    height = len(matrix)
    width = len(matrix[0])
    row = height - 1
    col = 0
    while col < width and row >= 0:
        if matrix[row][col] > loss_value:
            row -= 1
        elif matrix[row][col] < loss_value:
            col += 1
        else:
            return [row, col]

    return [-1, -1]


def main():
    matrix = [
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [3, 7, 11, 15],
        [4, 8, 12, 16]
    ]

    loss_value = 10

    print(determine_location(matrix, loss_value))


main()
