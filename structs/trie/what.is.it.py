"""
In the previous section, we covered several common types of trees like Red-Black trees, 2-3 trees, etc.

Now, we are going to look at a tree-like data structure that proves to be really efficient while solving programming
problems related to strings.

This data structure is called a trie and is also known as a Prefix Tree. We will soon find out why.

The tree trie is derived from “retrieval.” As you can guess, the main purpose of using this structure is to provide
 fast retrieval. Tries are mostly used in dictionary word searches, search engine auto-suggestions, and IP
 routing as well.

Autocomplete
Contact searching
"""


class TrieNode:
    def __init__(self, char=''):
        self.char = char
        # depending on the size of the alphabet
        self.children = [None] * 26
        self.is_end_word = False

    def mark_as_leaf(self):
        self.is_end_word = True

    def unmark_as_leaf(self):
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, t):
        """helper to get the index of a letter"""
        return ord(t) - ord('a')

    def insert(self, key):
        if key is None:
            return

        key = key.lower()
        idx = 0
        cur = self.root

        while idx < len(key):
            letter_index = self.get_index(key[idx])
            if cur.children[letter_index] is None:
                cur.children[letter_index] = TrieNode(key[idx])

            cur = cur.children[letter_index]
            idx += 1

        cur.mark_as_leaf()
        return True

    def search(self, key):
        if key is None:
            return False

        key = key.lower()
        cur = self.root
        idx = 0

        while idx < len(key):
            letter_index = self.get_index(key[idx])

            if cur.children[letter_index] is None:
                return False

            cur = cur.children[letter_index]
            idx += 1

        return cur.is_end_word

    def has_no_children(self, node):
        for child in node.children:
            if child is not None:
                return False

        return True

    # def delete(self, key):
    #     def del_helper(cur, key, idx=0):
    #         if idx < len(key):
    #             if self.get_index(key[idx]) in cur.children:
    #                 del_helper(cur[self.get_index(key[idx])], key, idx + 1)
    #                 if


def main():
    trie = Trie()
    trie.insert('able')
    print(trie.search('able'))


main()
