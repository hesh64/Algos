"""BBNNC -> BNBCN"""

from heapq import *

"""A nice rule to know is if a value frequency is more than (n + 1) / 2"""

# todo has a bug

# O(n) Time and Space
def resultant_order(str):
    map = {}
    join, heap = [], []
    n = len(str)

    for c in str:
        if c not in map:
            map[c] = 0
        map[c] += 1

    for k in map:
        if (n + 1) / 2 < map[k]:
            return str

        heappush(heap, (-map[k], k))

    while len(heap):
        count, letter = heappop(heap)
        join.append(letter)
        if count != -1:
            heappush(heap, (count + 1, letter))

    return ''.join(join)


def main():
    str = 'bbnnc'
    result = resultant_order(str)
    print(result)
    str = 'aab'
    result = resultant_order(str)
    print(result)


main()
