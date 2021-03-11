def find_word(grid, words):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # O(L) where l in the length of the word
    def dfs(g, r, c, chars, v):
        if v[r][c]:
            return False
        else:
            v[r][c] = True
            chars[ord(g[r][c]) - ord('A')] -= 1
            # this is o(1) because it's fixed size.
            if sum(chars) == 0:
                return True

            """
                you will always go in three of the 4 directions

                3 ^ L

            """
            if 0 <= r - 1 < len(g) \
                    and visited[r - 1][c] is False \
                    and chars[ord(g[r - 1][c]) - ord('A')] > 0:
                if dfs(g, r - 1, c, chars, v):
                    return True

            if 0 <= r + 1 < len(g) \
                    and visited[r + 1][c] is False \
                    and chars[ord(g[r + 1][c]) - ord('A')] > 0:
                if dfs(g, r + 1, c, chars, v):
                    return True

            if 0 <= c - 1 < len(g[0]) \
                    and visited[r][c - 1] is False \
                    and chars[ord(g[r][c - 1]) - ord('A')] > 0:
                if dfs(g, r, c - 1, chars, v):
                    return True

            if 0 <= c + 1 < len(g[0]) \
                    and visited[r][c + 1] is False \
                    and chars[ord(g[r][c + 1]) - ord('A')] > 0:
                if dfs(g, r, c + 1, chars, v):
                    return True

            chars[ord(g[r][c]) - ord('A')] += 1
            v[r][c] = False
            return False

    found = []
    for word in words:
        letters = [0] * 26
        for l in word:
            char = ord(l) - ord('A')
            letters[char] += 1

        # O(L * (n * 3 ^ L)) where n is the nubmer of letters in a grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == word[0]:
                    # O(3^L)
                    if dfs(grid, row, col, letters, visited):
                        found.append(word)
    return found


"""
we can do better that that

use a Trie!
"""


def main():
    grid = [['B', 'S', 'L', 'I', 'M'],
            ['R', 'I', 'L', 'M', 'O'],
            ['O', 'L', 'I', 'E', 'O'],
            ['R', 'Y', 'I', 'L', 'N'],
            ['B', 'U', 'N', 'E', 'C']]
    words = ["BUY", "SLICK", "SLIME", "ONLINE", "NOW"]
    print(find_word(grid, words))


main()
