from functools import lru_cache


@lru_cache(None)
def decompose(ws, s):
    if 0 == len(s):
        return True

    for w in ws:
        if s.startswith(w) and decompose(ws, s[len(w):]):
            return True

    return False


words = tuple(['a', 'man', 'canal', 'plan'])
word = 'mancanalaplan'
print(decompose(words, word))
