def break_query(query, words):
    n = len(query)
    dp = [False for _ in range(n + 1)]
    dp[0] = True

    for i in range(n):
        if dp[i]:
            for key in words:
                l = len(key)
                if i + l <= n and query[i: i + l] == key:
                    dp[i + l] = True
                    break

    return dp[0]


d = []


def query_splitter(query, words):
    i, str, store = 0, '', []
    query_splitter_helper(query, words, i, str, store)
    return store


def query_splitter_helper(query, words, i, cur, store):
    if i > len(query):
        return False

    if i == len(query):
        store.append(cur)

    for word in words:
        if i + len(word) <= len(query) and query[i: i + len(word)] == word:
            query_splitter_helper(query, words, i + len(word), word if len(cur) == 0 else cur + ' ' + word, store)

    return store


def main():
    query = "vegancookbook"
    dict = ["i", "cream", "cook", "scream", "ice", "cat", "book", "icecream", "vegan", 'veg', 'an']
    print(query_splitter(query, dict))

    query = "vegancookbook"
    dict = ["an", "book", "car", "cat", "cook", "cookbook", "crash",
            "cream", "high", "highway", "i", "ice", "icecream", "low",
            "scream", "veg", "vegan", "way"]
    print(query_splitter(query, dict))

    query = "highwaycarcrash"
    print(query_splitter(query, dict))


main()
