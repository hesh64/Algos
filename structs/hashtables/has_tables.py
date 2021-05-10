import functools


def string_hash(s, modulus):
    mult = 997
    return functools.reduce(lambda v, c: (v * mult + ord(c)) % modulus, s, 0)


print(string_hash('salim', 1000))
print(string_hash('alim1', 1000))

from collections import Counter


def is_palindromic(string):
    counts = Counter(string)
    return sum(1 for k in counts if counts[k] % 2 != 0) <= 1


print('\n\nis_palindromic')
print(is_palindromic('aba'))
print(is_palindromic('abaa'))
print(is_palindromic('abccba'))
print(is_palindromic('abcdcba'))
print(is_palindromic('0bcdcba'))


# O(l + m)
def can_write_anonymous_letter_with_magazine(letter, magazine):
    mag_count = Counter(magazine)
    letter_count = Counter(letter)
    return all(k in mag_count and letter_count[k] <= mag_count[k] or False
               for k in letter_count)


# O(l + m) but more elegant-- we stop once we saw l letters from letter in magazine
def can_write_anonymous_letter_with_magazine2(letter, magazine):
    letter_count = dict(Counter(letter))
    for c in magazine:
        if c in letter_count:
            letter_count[c] -= 1
            if letter_count[c] == 0:
                del letter_count[c]
                if len(letter_count) == 0:
                    return True

    return len(letter_count) == 0


letter = '''Dear world how are you on this fine day?'''
magazine = '''Dear world how are you so cruel, to this day I am not fine?'''
print('\n\ncan_write_anonymous_letter_with_magazine')
print(can_write_anonymous_letter_with_magazine(letter, magazine))
print(can_write_anonymous_letter_with_magazine2(letter, magazine))

from collections import OrderedDict

print('\n\nISBNCache')


class ISBNCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def insert(self, isbn, price):
        if isbn in self.cache:
            self.cache.pop(isbn)
        elif len(self.cache) == self.capacity:
            # pop the oldest
            self.cache.popitem(last=False)

        self.cache[isbn] = price

    def lookup(self, isbn):
        if isbn not in self.cache:
            return -1

        price = self.cache.pop(isbn)
        self.cache[isbn] = price

        return price

    def erase(self, isbn):
        return self.cache.pop(isbn, None) is None


isbns = ISBNCache(10)
isbns.insert("s1", 145)
isbns.insert("s2", 143)
print(isbns.lookup('s2'))
isbns.insert("s2", 1431)
print(isbns.lookup('s2'))
isbns.erase(1)

print('closest entries in a paragraph')


def closest(words):
    word, min_dist = None, len(words) + 1
    cache = {}
    for i, w in enumerate(words):
        if w in cache:
            if i - cache[w] < min_dist:
                min_dist = i - cache[w]
                word = w
        cache[w] = i

    return min_dist, word


print(closest(['All', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'work', 'no', 'fun', 'and', 'no', 'results']))

# edges = [[0, 1], [2, 0], [2, 1], [2, 3], [3, 1], [4, 5], [5,7], [7,4]]
edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 2]]


def count_triangles(n, edges):
    count = 0
    g = {i: [] for i in range(n)}
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    for v0 in range(n):
        for v1 in g[v0]:
            for v2 in g[v1]:
                for v3 in g[v2]:
                    if v3 == v0:
                        count += 1

    return count // 6


print('\n\nedges')
print(count_triangles(4, edges))

print('\n\n')
paragraph = '''
My paramount object in this struggle is to save the Union, and is not either to save or to destroy slavery. If I could save the Union without freeing any slave I would do it, and if I could save it by freeing all the slaves I would do it; and if I could save it by freeing some and leaving others alone I would also do that
'''
words = {'save', 'Union'}


def find_shortest_substring_containing_set(par, words):
    counter = {}
    for w in words:
        counter[w] = 0

    not_found = len(counter)
    par = par.replace(',', '')
    par = par.replace('.', '')
    par_words = par.split(' ')
    start, end = 0, len(par_words)

    for i, word in enumerate(par_words):
        if word in counter:
            counter[word] += 1
            if counter[word] == 1:
                not_found -= 1
                if not_found == 0:
                    end = i
                    break

    while start < end:
        w = par_words[start]
        if w in counter:
            if counter[w] > 1:
                counter[w] -= 1
            else:
                break
        start += 1

    while start < end:
        w = par_words[end]
        if w in counter:
            if counter[w] > 1:
                counter[w] -= 1
            else:
                break
        end -= 1

    return start, end


print(find_shortest_substring_containing_set(paragraph, words))


def largest_consecutive_interval(values):
    s = set(values)
    largest = -1
    largest_ax = []

    while s:
        value = s.pop()
        count, lower, upper = 1, value - 1, value + 1

        # add on
        ax = [value]
        while lower in s:
            # add on
            ax.append(lower)
            count += 1
            s.remove(lower)
            lower -= 1

        while upper in s:
            # add on
            ax.append(upper)
            count += 1
            s.remove(upper)
            upper += 1

        if count > largest:
            largest, largest_ax = count, ax
        largest = max(largest, count)

    return largest, largest_ax


print('\n\nlargest_consecutive_interval')
print(largest_consecutive_interval([10, 5, 3, 11, 6, 100, 4]))

from functools import lru_cache
import sys

sys.setrecursionlimit(15000)


@lru_cache(None)
def collatz_conjecture(n):
    if n == 1:
        return [1]
    if n % 2 != 0:
        return [n] + collatz_conjecture(n * 3 + 1)
    else:
        return [n] + collatz_conjecture(n // 2)


[collatz_conjecture(i) for i in range(10 ** 6, 1, -1)]
# print('done', )
# collatz_conjecture(10 ** 9)
