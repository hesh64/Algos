"""
Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.
"""

from heapq import *


# worst case is O(nlog(n)) -> where all the letters are distinct
# space O(n)
def rearrange(string):
    freq = {}
    # O(n)
    for s in string:
        if s not in freq:
            freq[s] = 0
        freq[s] += 1

    min_heap = []
    # O(k * log(k))
    [heappush(min_heap, (-f, letter)) for letter, f in freq.items()]

    new_word = []
    # O(n * log(k)) where n is string length, k is number of distinct letters
    for _ in range(len(string)):
        f, letter = heappop(min_heap)
        f = -f

        if len(new_word) and new_word[-1] == letter:
            return False

        new_word.append(letter)

        if f - 1 > 0:
            heappush(min_heap, (-f + 1, letter))

    return ''.join(new_word)


def main():
    word = 'aappp'
    result = rearrange(word)
    print(result)


main()
