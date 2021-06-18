class UnionSet:
    def __init__(self, x):
        self.x = x
        self.p = self


class UnionForest:
    def __init__(self):
        self.sets = {}

    def make_set(self, x):
        if x not in self.sets:
            self.sets[x] = UnionSet(x)

    def find(self, x):
        if self.sets[x] != self.sets[x].p:
            return self.find(self.sets[x].p)

        return self.sets[x].x

    def union(self, x, y):
        if self.find(x) != self.find(y):
            self.sets[y].p = self.sets[x]

def find_path(f, x):
    values = []
words = ['top', 'dog','fog', 'fig']
start = 'top'
end = 'fig'
