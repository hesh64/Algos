def word_break(s, words):
    def dfs(i):
        if i == len(s):
            return True

        for word in words:
            if s[i:].startswith(word):
                if dfs(i + len(word)):
                    return True

    return dfs(0)


def word_break_dp(s, words, dp):
    def dfs(i):
        if i == len(s):
            return True

        for word in words:
            if s[i:].startswith(word):
                if s[i:] not in memo:
                    memo[s[i:]] = dfs(i + len(word))

                return memo[s[i:]]
        return False

    return dfs(0)


inputs = ["algomonster", "aab",
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"]
inputs2 = ["algo monster", "a c", "a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa"]
# for i in range(len(inputs)):
#     print("Word break : ", word_break(inputs[i], inputs2[i]))

for i in range(len(inputs)):
    memo = {}
    print("Word break : ", word_break_dp(inputs[i], inputs2[i], memo))
