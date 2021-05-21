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
        if x not in self.sets:
            self.sets[x] = UnionSet(x)

    def find_set(self, x):
        if self.sets[x] != self.sets[x].p:
            self.sets[x].p = self.find_set(self.sets[x].p.x)
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


def link_accounts():
    accounts = [["Sarah", "sarah22@email.com", "sarah@gmail.com", "sarahhoward@email.com"],
                ["Alice", "alicexoxo@email.com", "alicia@email.com", "alicelee@gmail.com"],
                ["Sarah", "sarah@gmail.com", "sarah10101@gmail.com"],
                ["Sarah", "sarah10101@gmail.com", "misshoward@gmail.com"]
                ]

    email_to_name = {}
    name_to_emails = {}
    forest = UnionForest()
    for account in accounts:
        for i in range(1, len(account)):
            forest.make_set(account[i])
            email_to_name[forest.find_set(account[i]).x] = account[0]
            if i > 1:
                forest.union(account[i - 1], account[i])

    """
    yes i grouped them by name, but in reality that's a trivial detail. Instead of storing just the email
    in the set, store a tuple(email, name) or named tuple then just reference that from the parent set
    badabing badaboom
    """
    for s in forest.sets:
        parent_key = email_to_name[forest.find_set(s).x]
        if parent_key not in name_to_emails:
            name_to_emails[parent_key] = []
        name_to_emails[parent_key].append(s)

    return [[name, *emails] for name, emails in name_to_emails.items()]


print(link_accounts())

forest = UnionForest()
# n sets
forest.make_set('a')
forest.make_set('b')
forest.make_set('c')
# n-1 unions
forest.union('c', 'b')
forest.union('b', 'a')
print(forest)
