"""

Given a string, sort it based on the decreasing frequency of its characters
"""
from heapq import *


class FreqTuple:
    def __init__(self, letter, count):
        self.letter, self.count = letter, count

    def __lt__(self, other):
        return self.count < other.count


# time O(n log(n)) where n is the number of distinct characters
# space O(n) n number of distinct characters we are storing
def freq_sort(word):
    freq = {}
    max_heap = []

    # O(n)
    for l in word:
        if l not in freq:
            freq[l] = 0
        freq[l] -= 1

    # O(n * log(n))
    [heappush(max_heap, FreqTuple(k, v)) for k, v in freq.items()]

    new_letters = []
    # O(n)
    while len(max_heap):
        item = heappop(max_heap)
        # we can switch this to a q, to get a better read. But
        # new_letters.append(item.letter * -item.count)
        for _ in range(-item.count):
            new_letters.append(item.letter)

    return ''.join(new_letters)


def main():
    word = 'Programming'
    result = freq_sort(word)
    print(result)


main()
