# O(n * k) Time
# O(n * k) Space

"""group words using anagrams"""


def group_titles(strs):
    res = {}
    for s in strs:
        count = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            count[index] += 1
        key = tuple(count)
        if key in res:
            res[key].append(s)
        else:
            res[key] = [s]

    return res.values()


def main():
    titles = ["duel", "dule", "speed", "spede", "deul", "cars"]
    gt = list(group_titles(titles))
    print(gt)
    query = 'spede'
    for g in gt:
        if query in g:
            print(g)


main()
