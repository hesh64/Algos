def can_sum_memo(val, lis, memo=dict()):
    if val in memo:
        return memo[val]
    if val == 0:
        return True
    if val < 0:
        return False

    for ele in lis:
        rem = val - ele
        res = can_sum_memo(rem, lis, memo)
        if rem >= 0:
            memo[rem] = res
            if memo[rem]:
                return memo[rem]

    return False


print(can_sum_memo(7, [5, 4, 3, 7]))


# print(can_sum_memo(300, [14, 7]))
# print(can_sum_memo(1000, [1, 111, 4]))
# print(can_sum_memo(10666, [10000, 111, 4]))

def can_sum_tabulation(target, lis):
    table = [False] * (target + 1)
    table[0] = True

    for i in range(len(table)):
        if table[i]:
            for num in lis:
                if i + num < len(table):
                    table[i + num] = True

    return table[target]


print(can_sum_tabulation(7, [5, 4, 3, 7]))
print(can_sum_memo(106661, [100000, 666, 1, 6, 111, 4]))