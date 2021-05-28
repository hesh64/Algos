def find_shapes(m):
    def get_shape(row, col, offr, offc, co, vis):
        co.append((offr, offc))
        vis.add((row, col))

        for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            rowr, colc = row + r, col + c
            if 0 <= rowr < len(m) and 0 <= colc < len(m[0]) \
                    and m[rowr][colc] == 1 and (rowr, colc) not in vis:
                get_shape(rowr, colc, offr + r, offc + c, co, vis)

        return tuple(co)

    counts = {}
    visited = set()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1 and (i, j) not in visited:
                shape = get_shape(i, j, 0, 0, [], visited)
                if shape not in counts:
                    counts[shape] = 0
                counts[shape] += 1

    return 0 if len(counts) == 0 else max(counts.values())


m = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
res = find_shapes(m)
print(m, res)

print('\n')
m = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
]
res = find_shapes(m)
print(m, res)

print('\n')

m = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
]
res = find_shapes(m)
print(m, res)

print('\n')
m = [
    [0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1],
]
res = find_shapes(m)
print(m, res)
