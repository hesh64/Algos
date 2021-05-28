class UnionSet:
    def __init__(self, x):
        self.x = x
        self.r, self.p = 0, self


class UnionForest:
    def __init__(self):
        self.sets = {}

    def make_set(self, x):
        if x not in self.sets:
            self.sets[x] = UnionSet(x)

    def union(self, x, y):
        if self.find_set(x) != self.find_set(y):
            self.link(x, y)

    def find_set(self, x):
        if self.sets[x] != self.sets[x].p:
            self.sets[x].p = self.find_set(self.sets[x].p.x)

        return self.sets[x].p

    def link(self, x, y):
        if self.sets[x].r > self.sets[y].r:
            self.sets[y].p = self.sets[x]
        else:
            self.sets[x].p = self.sets[y]
            if self.sets[x].r == self.sets[y].r:
                self.sets[y].r += 1


def dedupe(ids):
    forest = UnionForest()
    # iterating over all the items is alpha(n)
    for k in ids:
        names = ids[k]
        for i in range(len(names)):
            forest.make_set(names[i])
            if i > 0:
                forest.union(names[i], names[i - 1])

    set_to_ids = {}
    # iterating over the sets at most m - n
    for k in ids:
        pset = forest.find_set(ids[k][0])
        if pset not in set_to_ids:
            set_to_ids[pset] = set()
        set_to_ids[pset].add(k)

    return set_to_ids.values()


idToNames = {
    1: ['bob', 'bobby'],
    2: ['bobby'],
    3: ['alice', 'a'],
    4: ['alice', 'ally'],
    5: ['alice', 'bob']
}

print(dedupe(idToNames))

idToNames = {
    1: ['bob', 'bobby'],
    2: ['bobby'],
    3: ['alice', 'a'],
    4: ['alice', 'ally'],
    5: ['alice', ]
}

print(dedupe(idToNames))
idToNames = {
    1: ['bob'],
    2: ['bobby'],
    3: ['a'],
    4: ['ally'],
    5: ['alice', ]
}

print(dedupe(idToNames))
