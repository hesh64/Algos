"""
Reconstructing a Sequence (hard) #
Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely
reconstructed from the array of sequences.

Unique reconstruction means that we need to find if originalSeq is the only sequence such that all
sequences in the array are subsequences of it.
"""
# O(V + E)
from collections import deque


def can_construct(originalSeq, sequences):
    sorted_order = []
    if len(originalSeq) == 0:
        return False

    in_degrees = {}
    graph = {}
    for s in sequences:
        # smart way to initialize
        for num in s:
            in_degrees[num] = 0
            graph[num] = []

    # take a sliding window of 2 items
    for sequence in sequences:
        for i in range(1, len(sequence)):
            # p - parent
            # c - child
            p, c = sequence[i - 1], sequence[i]
            in_degrees[c] += 1
            graph[p].append(c)

    # if the original_seq len isn't the same length of degrees
    # then something is wrong, and this surely wont construct
    # the list expected.
    if len(originalSeq) != len(in_degrees):
        return False

    # add your sources
    sources = deque()
    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)

    while sources:
        # if there are two keys in sources then there are more than
        # one ways to construct the list
        if len(sources) > 1:
            return False
        # if the very next value in the original list
        # isn't equal to the very next values in sources
        # then there is more than one way to construct the lsit
        if originalSeq[len(sorted_order)] != sources[0]:
            return False

        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)

    # if the sorted_order list and original sequence list length
    # isn't equal then there is more than one way to construct the
    # lists
    return len(sorted_order) == len(originalSeq)


def main():
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
          str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
