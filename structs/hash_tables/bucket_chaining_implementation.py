import random

random.seed(100)


class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.next_entry = None

    def __repr__(self):
        if self.next_entry is None:
            return f'{self.key}: {self.value} -> None'
        else:
            return f'{self.key}: {self.value} -> {self.next_entry}'


class HashTable:
    def __init__(self, slots):
        self.slots = slots
        self.size = 0

        self.buckets = [None] * self.slots

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    def get_index(self, key):
        hash_code = hash(key)
        return hash_code % self.slots

    def insert(self, key, value):
        index = self.get_index(key)
        entry = HashEntry(key, value)
        if self.buckets[index] is None:
            self.size += 1
            self.buckets[index] = entry
        else:
            cur = self.buckets[index]
            while cur.next_entry is not None:
                if cur.key == key and cur.value == value:
                    return None
                cur = cur.next_entry
            cur.next_entry = entry

        if (self.size / self.slots) >= .6:
            self.resize()

        return index

    def resize(self):
        new_slots = self.slots * 2
        new_buckets = [None] * new_slots

        for bucket in self.buckets:
            while bucket:
                new_index = self.get_index(bucket.key)
                new_entry = HashEntry(bucket.key, bucket.value)

                if new_buckets[new_index] is None:
                    new_buckets[new_index] = new_entry
                else:
                    cur = new_buckets[new_index]
                    while cur.next_entry is not None:
                        cur = cur.next_entry

                    cur.next_entry = new_entry

                bucket = bucket.next_entry

        self.slots = new_slots
        self.buckets = new_buckets

    def __repr__(self):
        ls = []

        for i, buck in enumerate(self.buckets):
            ls.append(f'{i}: {buck} \n')

        return ''.join(ls)


def main():
    ht = HashTable(10)

    for _ in range(1000):
        rand = random.randint(0, 1000000)
        ht.insert(rand, rand)
        print('Table state')
        print(ht)


main()
