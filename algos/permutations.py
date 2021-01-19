# n = len(chars)
# O(n!)
#
def permutation(chars, perms=[[]], level=0):
    if level == len(chars):
        return perms

    char = chars[level]
    new_perms = []

    for perm in perms:
        copy = perm.copy()
        copy.append(char)
        for i in range(len(copy)):
            copy2 = copy.copy()
            copy2[i], copy2[len(copy2) - 1] = copy2[len(copy2) - 1], copy2[i]
            new_perms.append(copy2)

    return permutation(chars, new_perms, level + 1)


print(permutation([]))
print(permutation(['a', 'b', 'c']))
print(permutation(['1', '2', '3', 'a', 'b', 'c']))
