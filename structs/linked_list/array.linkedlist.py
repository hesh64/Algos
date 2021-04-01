class TripleArrayDoubleLinkedList:
    next = 0
    cur = 1
    prev = 2

    def __init__(self):
        self.triple = [
            # next
            [None] * 10,
            # cur
            [None] * 10,
            # prev
            (['/'] + ([None] * 9))
        ]

        self.head = None

    def find_empty_slot(self) -> int:
        for i in range(len(self.triple[self.cur])):
            if self.triple[self.cur][i] is None:
                return i

        i = len(self.triple[self.next])
        self.triple[self.next].extend([None] * 10)
        self.triple[self.cur].extend([None] * 10)
        self.triple[self.prev].extend([None] * 10)
        return i

    def __get_next_index(self):
        if self.head is None:
            self.head = 0
            return 0

        i = self.head
        while self.triple[self.next][i] is not None:
            i = self.triple[self.next][i]

        new_idx = self.find_empty_slot()
        self.triple[self.next][i] = new_idx
        self.triple[self.prev][new_idx] = i
        return new_idx

    def insert(self, k):
        next_idx = self.__get_next_index()
        self.triple[self.cur][next_idx] = k


if __name__ == '__main__':
    ll = TripleArrayDoubleLinkedList()
    for i in range(15):
        ll.insert(i)

    for r in ll.triple:
        print(r)

