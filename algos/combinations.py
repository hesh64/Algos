# # Time: O(2^n)
# # Space: O(n^2)
# def combinations(items):
#     if len(items) == 0:
#         return [[]]
#
#     first = items[0]
#     rest = items[1:]
#     combs_without_first = combinations(rest)
#     combs_with_first = []
#     for c in combs_without_first:
#         copy = c[:]
#         copy.append(first)
#         combs_with_first.append(copy)
#
#     return combs_with_first + combs_without_first
#
#
# print(combinations([1, 2]))
# print(combinations(['a', 'b', 'c']))
#
# def permutation(chars, perms=[[]], level=0):
#     if level == len(chars):
#         return perms
#
#     char = chars[level]
#     new_perms = []
#
#     for perm in perms:
#         copy = perm.copy()
#         copy.append(char)
#         for i in range(len(copy)):
#             copy2 = copy.copy()
#             copy2[i], copy2[len(copy2) - 1] = copy2[len(copy2) - 1], copy2[i]
#             new_perms.append(copy2)
#
#     return permutation(chars, new_perms, level + 1)
#
# print(permutation([]))
# print(permutation(['a', 'b', 'c']))
# print(permutation(['1', '2', '3', 'a', 'b', 'c']))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def all_combination(chars):
    def all_(combo, chars, index=0):
        if index == len(chars):
            return [combo]

        left = all_(combo, chars, index + 1)
        right = all_(combo + chars[index: index + 1], chars, index + 1)
        return left + right

    return all_([], chars, 0)


chars = ['a', 'b', 'c']
r = all_combination(chars)
assert len(r) == 2 ** len(chars), 'there are 2 ** n combinations'
