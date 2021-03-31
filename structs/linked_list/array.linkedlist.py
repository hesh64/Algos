class DLLArray:
    def __init__(self, size):
        self.size = size
        self.key = [None] * size
        self.next = [None] * size
        self.prev = [None] * size

        self.l = None

    def insert(self, key):
        if self.l is None:
            self.l = 1
            self.key[1] = key
            return

        tmp = self.l
        while self.next[tmp]:
            tmp = self.next[tmp]

        index = 0
        while self.key[index] is not None:
            index += 1

        self.next[tmp] = index
        self.key[index] = key
        self.prev[index] = tmp


def main():
    keys = [1, 2, 3]
    dl = DLLArray(10)
    for k in keys:
        dl.insert(k)
        print('index', [i for i in range(dl.size)])
        print('key', dl.key)
        print('prev', dl.prev)
        print('next', dl.next)
        print()


main()
