from string import ascii_letters


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.s = {c: None for c in ascii_letters}


def add(T, w, i=0):
    if T is None:
        T = TrieNode()

    if i == len(w):
        T.is_word = True
    else:
        T.s[w[i]] = add(T.s[w[i]], w, i + 1)

    return T


def Trie(s):
    T = None

    for w in s:
        T = add(T, w)

    return T


def search(T, dist, w, i=0):
    # base case 1
    if i == len(w):
        if T is not None and T.is_word and dist == 0:
            return ''
        else:
            return None

    # base case 2
    if T is None:
        return None

    # exact match
    f = search(T.s[w[i]], dist, w, i + 1)
    if f is not None:
        return w[i] + f

    # base case 3
    if dist == 0:
        return None

    for c in ascii_letters:
        # insertion
        f = search(T.s[c], dist - 1, w, i)
        if f is not None:
            return c + f

        # substitution
        f = search(T.s[c], dist - 1, w, i + 1)
        if f is not None:
            return c + f

    # deletion
    return search(T, dist - 1, w, i)


def spell_check(T, w):
    assert T is not None
    dist = 0
    while True and dist < len(w):
        f = search(T, dist, w)
        if f is not None:
            return dist, f
        dist += 1


def main():
    s = ['port', 'pore', 'pre', 'pres', 'pret']
    T = Trie(s)

    res = spell_check(T, 'pre')
    print(res)

    res = spell_check(T, 'pri')
    print(res)

    res = spell_check(T, 'poop')
    print(res)

    res = spell_check(T, 'xxxxxx')
    print(res)


main()
