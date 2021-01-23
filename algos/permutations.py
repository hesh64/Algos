# n = len(chars)
# O(n!)
#
# there are n! permutations
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
#
# print(permutation([]))
# print(permutation(['a', 'b', 'c']))
# print(permutation(['1', '2', '3', 'a', 'b', 'c']))

def permutation(chars, perms=[[]], index=0):
    if index == len(chars):
        return perms

    char = chars[index]
    new_perms = []

    for perm in perms:
        copy = perm.copy()
        copy.append(char)
        for i in range(len(copy)):
            new = perm.copy()
            new.insert(i, char)
            new_perms.append(new)

    return permutation(chars, new_perms, index + 1)


def permute(nums, perms=[[]], index=0):
    if index == len(nums):
        return perms

    num = nums[index]
    new_perms = []

    for perm in perms:
        c = perm.copy()
        c.append(num)
        for i in range(len(c)):
            c2 = perm.copy()
            c2.insert(i, num)
            new_perms.append(c2)

    return permute(nums, new_perms, index + 1)


print(permutation([]))
print(permutation(['a', 'b', 'c']))
print(permute(['a', 'b', 'c']))
# print(len(permutation(['1', '2', '3', 'a', 'b', 'c'])), 6 * 5 * 4 * 3 * 2)
