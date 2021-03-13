from collections import deque


def possible_results(initial_word, final_word, word_group):
    g = {}
    l = len(initial_word)
    for word in word_group:
        for i in range(l):
            key = word[:i] + '_' + word[i + 1:]
            if key not in g:
                g[key] = []
            g[key].append(word)

    print('words')
    for key in g:
        print(key, g[key])
    print('')

    visited = {}
    stack = deque()
    for i in range(l):
        key = initial_word[:i] + '_' + initial_word[i + 1:]
        stack.append((key, [initial_word]))
        visited[key] = True

    result = []

    print('stack', stack)
    while stack:
        print(stack)
        key, lst = stack.popleft()
        if key in g:
            for child in g[key]:
                if child == final_word:
                    lst.append(child)
                    result.append(lst)

                print('child', child)
                for i in range(l):
                    new_key = child[:i] + '_' + child[i + 1:]
                    if new_key not in visited:
                        visited[new_key] = True
                        lst_copy = lst.copy()
                        lst_copy.append(child)
                        stack.append((new_key, lst_copy))

    return list(result)

    # for i in range(l):
    #     if key not in g:
    #         continue
    #
    #     for child in g[key]:
    #         if child == final_word:
    #             lst.append(final_word)
    #             result.append(lst)
    #         elif child not in visited:
    #             new_key = child[:i] + '_' + child[i:]
    #             if new_key in g:
    #                 new_lst = lst.copy()
    #                 new_lst.append(child)
    #                 stack.append((new_key, new_lst))

    return result


def main():
    initial_word = "hit"
    final_word = "cog"
    word_group = ["hot", "dot", "dog", "lot", "log", "cog"]

    print("The shortest sequece is of length:", possible_results(initial_word, final_word, word_group))


main()
