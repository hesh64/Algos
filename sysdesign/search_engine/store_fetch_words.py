LEN_ALPHABET = 26


class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.letters = [None] * LEN_ALPHABET
        self.word = False

    def is_word(self):
        return self.word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _get_index(self, char):
        return ord(char) - ord('a')

    def insert_word(self, word):
        cur = self.root
        for l in word:
            idx = self._get_index(l)
            if cur.letters[idx] is None:
                cur.letters[idx] = TrieNode(l)

            cur = cur.letters[idx]
        cur.word = True

    def search_word(self, word):
        cur = self.root
        for l in word:
            idx = self._get_index(l)
            if cur.letters[idx] is None:
                return False
            cur = cur.letters[idx]
        return cur.is_word()

    def starts_with(self, word):
        cur = self.root
        for l in word:
            idx = self._get_index(l)
            if cur.letters[idx] is None:
                return False
            cur = cur.letters[idx]

        return True


def main():
    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]
    print("Keys to insert: ")
    print(keys)

    d = Trie()

    for i in range(len(keys)):
        d.insert_word(keys[i])

    print("Searching 'there' in the dictionary results: " + str(d.search_word("there")))
    print("Searching the prefix 'by' in the dictionary results: " + str(d.starts_with("by")))


main()
