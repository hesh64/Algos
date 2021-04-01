"""
We can implement disjoint sets as objects that hold linked lists, and all that,

we are gonna be skipping that part, and just jump to disjoint forests as they are more efficient
once path compression is applied
"""


class DisjointItem:
    def __init__(self, key):
        self.key = key
        self.rank = 0
        self.p = self

    def __repr__(self):
        return f'{(self.key, self.rank)} -> {self.p if self.p != self else "Circulates"}'


# O(M alpha n)
class DisjointSetForest:
    def __init__(self):
        self.sets = set()

    def make_set(self, x):
        ds = DisjointItem(x)
        ds.p = ds
        ds.rank = 0
        self.sets.add(ds)
        return ds

    def find_set(self, x: DisjointItem):
        # secret sauce 2: on the way back from checking who your parent is, we'll update your .p pointer
        # to show he is your oldest ancestor! such that you your parent and siblings end up pointing
        # to the same object.
        if x.p != x:
            # on the way back from the top, your assigning the final parent to every node
            x.p = self.find_set(x.p)

        return x.p

    # Secret Sauce 1: Union by rank, if you have a lower rank you're automatically the child
    def link(self, x, y):
        if x.rank > y.rank:
            y.p = x
        else:
            x.p = y
            if x.rank == y.rank:
                y.rank += 1

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))


if __name__ == '__main__':
    df = DisjointSetForest()
    c = df.make_set('c')
    h = df.make_set('h')
    b = df.make_set('b')

    df.union(h, c)
    df.union(b, h)

    print(b)
    print(h)
