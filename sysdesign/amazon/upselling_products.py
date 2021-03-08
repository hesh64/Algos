from random import choice


class Product:
    def __init__(self):
        self.array = []
        self.table = {}

    # O(1) amortized
    def insert(self, key):
        if key in self.table:
            return False

        self.table[key] = len(self.array)
        self.array.append(key)

        return True

    # O(1) amortized
    def remove(self, key):
        if key in self.table:
            last_item, i = self.array[-1], self.table[key]
            self.array[i], self.table[last_item] = last_item, i
            self.array.pop()
            del self.table[key]
            return True

        return False

    # O(1)
    def get_random(self):
        return choice(self.array)


def main():
    # Driver code
    dataset = Product()
    dataset.insert(1212)
    dataset.insert(190)
    dataset.insert(655)
    dataset.insert(327)
    print(dataset.get_random())
    dataset.remove(190)
    dataset.remove(655)
    print(dataset.get_random())


main()
