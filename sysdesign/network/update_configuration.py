from collections import deque


# O(n) time and space
def update_configuration(grid):
    r, c = -1, -1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                r, c = row, col
                break

    que = deque()
    que.append((r, c))
    minutes = 0
    while que:
        size = len(que)

        for _ in range(size):
            row, col = que.popleft()
            grid[row][col] = 2
            if 0 <= row - 1 and grid[row - 1][col] == 1:
                que.append((row - 1, col))

            if 0 <= col - 1 and grid[row][col - 1] == 1:
                que.append((row, col - 1))

            if row + 1 < len(grid) and grid[row + 1][col] == 1:
                que.append((row + 1, col))

            if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                que.append((row, col + 1))

        minutes += 1

    return minutes - 1


def main():
    # Driver Code
    grid = [
        [1, 1, 0, 0, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 2, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1]]
    print(update_configuration(grid))


main()
