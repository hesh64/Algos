from typing import List


def intervalIntersection(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    i = j = 0

    merged = []

    while i < len(a) and j < len(b):
        lo = max(a[i][0], b[j][0])
        hi = min(a[i][1], b[j][1])

        if lo <= hi:
            merged.append([lo, hi])

        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1

    return merged


inputs = [
    [[0, 2], [5, 10], [13, 23], [24, 25]],
    [[1, 5], [8, 12], [15, 24], [25, 26]],
    [[1, 3], [5, 9]],
    [],
    [],
    [[4, 8], [10, 12]],
    [[1, 7]],
    [[3, 10]],
    [[8, 15]],
    [[2, 6], [8, 10], [12, 20]],
    [[8, 15], [100, 921]],
    [[2, 6], [8, 10], [12, 20]],
    [[100, 921]],
    [[2, 6], [8, 10], [12, 20]],
    [[4, 11]],
    [[1, 2], [8, 11], [12, 13], [14, 15], [17, 19]],
]

while inputs:
    item1, item2 = inputs.pop(0), inputs.pop(0)
    print(intervalIntersection(item1, item2))
