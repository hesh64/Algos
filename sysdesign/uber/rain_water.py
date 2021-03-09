# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [4, 2, 0, 3, 2, 5]

h = []
n = 0
left, right = height[0], height[2]
for i in range(1, len(height) - 1):

    left = max(left, height[i - 1])
    right = max(right, height[i + 1])

    around = min(left, right)
    if around > height[i]:
        n += around - height[i]

print(n)
