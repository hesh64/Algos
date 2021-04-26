import functools


def edit_distance(s1, s2):
    @functools.lru_cache(None)
    def fn(s1, i, s2, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if s1[i] != s2[j]:
            return 1 + min(
                fn(s1, i - 1, s2, j),  # delete
                fn(s1, i - 1, s2, j - 1),  # substitute
                fn(s1, i, s2, j - 1)  # add
            )

        return fn(s1, i - 1, s2, j - 1)

    return fn(s1, len(s1) - 1, s2, len(s2) - 1)


print(edit_distance('Saturday', 'Sundays'))
print(edit_distance('Salim', 'Saleem'))
# run this one without lru!
print(edit_distance('AABBCGGAGBCBCCCAAGCBCGAAAAGBCCGABCGAGACBCAGAAAAGGGGBCBCBCBCBCCBAGG',
                    'GAAAAGBBCBCCBAGGGABCGAGACBCAGAAAAAABBCGGAGCCGABCGAAABBCGGAGBCBCCCAAGCBCGAAAAGBCCGACBCAGAAAAGGGGBCBCBCGGBCBCBCBCBCCBAGG'))
