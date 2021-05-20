class UnionSet:
    def __init__(self, x):
        self.p = self
        self.x = x
        self.rank = 0

    def __str__(self):
        return f'{self.x} -> *' if self.p == self else f'{self.x} -> {self.p}'


class UnionForest:
    def __init__(self):
        self.sets = {}

    def make_set(self, x):
        self.sets[x] = UnionSet(x)

    def find_set(self, x):
        if self.sets[x] != self.sets[x].p:
            self.sets[x].p = self.find_set(self.sets[x].p)
        return self.sets[x].p

    def union(self, x, y):
        if self.find_set(x) != self.find_set(y):
            self.link(x, y)

    def link(self, x, y):
        if self.sets[x].rank < self.sets[y].rank:
            self.sets[x].p = self.sets[y]
        else:
            self.sets[y].p = self.sets[x]
            if self.sets[y].rank == self.sets[x].rank:
                self.sets[x].rank += 1

    def __str__(self):
        s = ''
        for k in self.sets:
            s += str(self.sets[k]) + '\n'

        return s


def init():
    forest = UnionForest()

    names = [['a', 'b', 'c'], ['e', 'f', 'g', 'h']]
    for n in names:
        forest.make_set(n[0])
        for ni in n[1:]:
            forest.make_set(ni)
            forest.union(n[0], ni)

    print(forest)


init()
