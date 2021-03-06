def dfs(friends, n, visited, v):
    for x in range(n):
        if x != v and visited[x] == 0 and friends[v][x] == 1:
            visited[x] = 1
            dfs(friends, n, visited, x)


# since it's an n x n
# The time complexity will be o(n^2)
# the max number of friends a user can have is n - 1
# so the max depth of the rec stack will be n
def friend_circles(friends, n):
    if len(friends) == 0:
        return 0

    num_circles = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(friends, n, visited, i)
            num_circles += 1

    return num_circles


def main():
    n = 4
    friends = [
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1]
    ]

    print('the number of frined circles is:', friend_circles(friends, n))


main()
