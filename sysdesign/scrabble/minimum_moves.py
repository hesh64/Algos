from collections import deque


def minimum_moves(initial_word, final_word, word_group):
    g = {}
    # all words are the same length
    n = len(initial_word)
    for word in word_group:
        for i in range(n):
            key = word[:i] + '_' + word[i + 1:]
            if key not in g:
                g[key] = []
            g[key].append(word)

    print(g)
    # to get from the first word to the last word
    # in the shorted distance we can bfs
    que = deque()
    for i in range(n):
        que.append(initial_word[:i] + '_' + initial_word[i + 1:])
    levels = 1

    while que:
        size = len(que)
        for _ in range(size):
            node = que.popleft()
            if node not in g:
                continue
            for child in g[node]:
                if child == final_word:
                    return levels
                for i in range(n):
                    que.append(child[:i] + '_' + child[i + 1:])

        levels += 1

    return -1


def main():
    initial_word = "hit"
    final_word = "cog"
    word_group = ["hot", "dot", "dog", "lot", "log", "cog"]

    print("The shortest sequece is of length:", minimum_moves(initial_word, final_word, word_group))


main()
