# s = '_thou shall not'
# t = '_you should not'
#
# from functools import lru_cache
#
#
# def edit_dist(s, t):
#     i, j = len(s) - 1, len(t) - 1
#
#     @lru_cache(None)
#     def helper(i, j):
#
#         if i == 0:
#             return j
#         if j == 0:
#             return i
#
#         return min(
#             helper(i - 1, j - 1) + (1 if s[i] != t[j] else 0),
#             helper(i, j - 1) + 1,
#             helper(i - 1, j) + 1
#         )
#
#     return helper(i, j)
#
#
# print(edit_dist(s, t))
#
#
# def edit_dist_tab(s, t):
#     # init a matrix that represents the movement in decisions made
#     dp = [[0 for _ in range(len(t))] for _ in range(len(s))]
#
#     # initialize the edges fo the matrix to support /represent the type of
#     # cost associated with i 0 or j 0
#     for i in range(len(s)):
#         dp[i][0] = i
#
#     for j in range(len(t)):
#         dp[0][j] = j
#
#     # swap the basing int count with an object to maintain the path  taken
#     for i in range(1, len(s)):
#         for j in range(1, len(t)):
#             dp[i][j] = min(
#                 dp[i - 1][j - 1] + (1 if s[i] != t[j] else 0),
#                 dp[i - 1][j] + 1,
#                 dp[i][j - 1] + 1
#             )
#
#     # change this to return the goal cell we want
#     return dp[len(s) - 1][len(t) - 1]
#
#
# print(edit_dist_tab(s, t))

# from collections import defaultdict
#
# s = [100, 200, 300, 400, 500, 600, 700, 800, 900]
#
#
# def partition(s, k):
#     def cost(a, b):
#         return abs((a * a) - (b * b))
#
#     partition = [None] * len(s)
#
#     def sum_partitions(s, partitions):
#         d = defaultdict(int)
#
#         for i in range(len(partitions)):
#             d[i] += s[i]
#
#         return sum(list(d.values())) / len(d)
#
#     global_avg = sum(s) / k
#     global_cost = float('inf')
#     best_partition = None
#
#     def helper(i, p):
#         nonlocal global_cost, global_avg, best_partition
#
#         if i == len(s):
#             avg = sum_partitions(s, partition)
#             if cost(global_avg, avg) < global_cost:
#                 global_cost = avg
#                 best_partition = partition[:]

s = [1, 2, 1, 2]


def gen_perm(s):
    in_perm = {}

    def backtrack(s, k):

