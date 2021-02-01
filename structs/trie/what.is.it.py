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


class TrieNOde:
    def __init__(self, char=''):
        self.char = char
        # depending on the size of the alphabet
        self.children = [None] * 26
        self.is_end_word = False

    # def mark_as_leaf(self):
