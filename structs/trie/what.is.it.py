from collections import deque


class TrieNode:
    def __init__(self, char=''):
        self.char = char
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
        return ord(t) - ord('a')

    # Time O(n) where n is len(key)
    def insert(self, key):
        if key is None:
            return

        key = key.lower()
        cur_node = self.root
        index = 0

        for level in range(len(key)):
            index = self.get_index(key[level])
            if cur_node.children[index] is None:
                cur_node.children[index] = TrieNode(key[level])

            cur_node = cur_node.children[index]

        print(cur_node.char)

        cur_node.mark_as_leaf()

    def search(self, key):
        if key is None:
            return None

        key = key.lower()
        cur_node = self.root

        for level in range(len(key)):
            index = self.get_index(key[level])
            if cur_node.children[index] is None:
                return False

            cur_node = cur_node.children[index]

        # print(53)
        if cur_node is not None and cur_node.is_end_word:
            return True

        return False

    def has_no_children(self, current_node):
        for i in range(len(current_node.children)):
            if current_node.children[i] is not None:
                return False
        return True

    def delete_helper(self, key, current_node, length, level):
        deleted_self = False

        if current_node is None:
            return deleted_self

        if level == length:
            if self.has_no_children(current_node):
                current_node = None
                deleted_self = True
            else:
                current_node.unmark_as_leaf()
                deleted_self = False
        else:
            child_node = current_node.children[self.get_index(key[level])]
            child_deleted = self.delete_helper(key, child_node, length, level + 1)

            if child_deleted:
                current_node.children[self.get_index(key[level])] = None

                if current_node.is_end_word:
                    deleted_self = False

                elif self.has_no_children(current_node) is False:
                    deleted_self = False

                else:
                    current_node = None
                    deleted_self = True
            else:
                deleted_self = False

        return deleted_self

    def delete(self, key):
        if self.root is None or key is None:
            return None

        self.delete_helper(key, self.root, len(key), 0)


# O(n)
def total_words(root):
    if not root:
        return 0

    count = 0
    if root.is_end_word:
        count += 1

    return count + sum([total_words(child) for child in root.children if child is not None])


# time O(n)
def total_words_itr(root):
    count = 0
    q = deque()

    for child in root.children:
        if child:
            q.append(child)
    while q:
        cur = q.popleft()
        if cur.is_end_word:
            count += 1
        for child in cur.children:
            if child:
                q.appendleft(child)

    return count


# O(n)
def sort_list(list):
    trie = Trie()

    for word in list:
        trie.insert(word)

    return find_words(trie.root)


# time O(n)
def find_words(root):
    words = []
    stack = []

    def _find_words(root, stack):
        stack.append(root.char)
        if root.is_end_word:
            words.append(''.join(stack))

        for child in root.children:
            if child:
                _find_words(child, stack)

        stack.pop()

    _find_words(root, stack)
    return words

def is_formation_possible(list, word):
    trie = Trie()

    for word in list:
        trie.insert(word)

    start = 0


def main():
    t = Trie()

    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]

    for key in keys:
        t.insert(key)

    print('\n')

    b = t.get_index('b')
    y = t.get_index('y')
    e = t.get_index('e')
    print(t.root.children[b].char)
    print(t.root.children[b].is_end_word)
    print(t.root.children[b].children[y].char)
    print(t.root.children[b].children[y].is_end_word)
    print(t.root.children[b].children[y].children[e].char)
    print(t.root.children[b].children[y].children[e].is_end_word)

    print(t.search('bye'))
    for key in keys:
        print(f'Is the word "{key}" in trie? {t.search(key)}')

    print(t.search('bye'))
    print(t.delete('bye'))
    print(t.search('bye'))

    print(f'trie has {total_words(t.root)} words')
    print(f'trie has {total_words_itr(t.root)} words')

    words = find_words(t.root)
    print('words in sorted order: ', words)
    print(f'sorted list: {keys} result: {sort_list(keys)}')


main()
