def len_repeated(s, i):
    temp = i
    while temp < len(s) and s[i] == s[temp]:
        temp += 1

    return temp - i


# s is longer
# w is the word
def flag_word(s, w):
    if not s or not w:
        return False
    i, j = 0, 0
    while i < len(s) and j < len(w):
        if s[i] == w[j]:
            len1 = len_repeated(s, i)
            len2 = len_repeated(w, j)

            if (len1 < 3 and len1 != len2) or (3 <= len1 < len2):
                return False

            i += len1
            j += len2
        else:
            return False

    return i == len(s) and j == len(w)
