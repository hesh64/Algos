"""Given a large array of integers and a window of size ww, find the current maximum value in the window as the window slides through the entire array.

Let’s try to find all maximums for a window size equal to 33 in the array given below:"""
from collections import deque

# a, k = [-4, 2, -5, 3, 6], 3
a, k = [-4, 2, -5, 3, 6], 3


def max_in_sliding_window(a, k):
    que, res = deque(), []

    for end in range(len(a)):
        while len(que) > 0 and a[end] > a[que[-1]]:
            que.pop()
        que.append(end)

        if len(que) and end - k + 1 > que[0]:
            que.popleft()

        if len(que) and end - k + 1 >= 0:
            res.append(a[que[0]])
    return res


print(max_in_sliding_window(a, k))
a, k = [-4, 2, -5, 3, 6], 2

print(max_in_sliding_window(a, k))

a, k = [-4, 2, -5, 3, 6], 1
print(max_in_sliding_window(a, k))

a, k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3
print(max_in_sliding_window(a, k))

