class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.data = None
        self.rank = 0


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keyword = ''
        for i in range(len(sentences)):
            self.add_record(sentences[i], times[i])

    def add_record(self, word, hot=0):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
        cur.data = word
        cur.rank -= hot

    def search_word(self, word):
        cur = self.root
        for l in word:
            if l not in cur.children:
                return []
            cur = cur.children[l]
        return self.dfs(cur)

    def dfs(self, node):
        res = []
        if node.is_end:
            res.append((node.rank, node.data))

        for child in node.children:
            res.extend(self.dfs(node.children[child]))

        return res

    def autocomplete(self, w):
        results = []
        if w == '#':
            self.keyword = ''
        else:
            self.keyword += w
            results = self.search_word(self.keyword)

        return [i[1] for i in sorted(results)][:3]


def main():
    # Driver code
    sentences = ["beautiful", "best quotes", "best friend", "best birthday wishes", "instagram", "internet"]
    times = [30, 14, 21, 10, 10, 15]
    auto = AutocompleteSystem(sentences, times)
    print(auto.autocomplete("b"))
    print(auto.autocomplete("e"))
    print(auto.autocomplete("s"))
    print(auto.autocomplete("t"))
    print(auto.autocomplete("#"))


main()
