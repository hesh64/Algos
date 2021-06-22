# find the longest increasing subsequence
s = [
    2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
    # 2, 4, 3, 5, 1, 7, 6, 9, 8,
]


# O(n^2)
def longest_tab(s):
    # pass the sequence to make it play nicer with indices
    s = [None] + s
    # initialize the lengths array
    lens = [1] * len(s)
    # if we need to reconstruct the sequence then we need predecessors array
    pred = [None] * len(s)

    for i in range(1, len(s)):
        # the first element before i is i - 1
        j = i - 1
        while j > 0:
            # we only look at smaller elements not smaller than or equal to
            if s[j] < s[i]:
                # if we want to find the first predecessor keey the >= because
                # it will update the value again once we see another equal value
                # in our case that would case 4 to be a predecessor instead of 3
                # because they both have a length of 1 but 4 shows up after 3
                # so it will retrigger the condition.
                # but if we change it to > we get 3 selected as the pred.
                if lens[j] + 1 >= lens[i]:
                    lens[i] = lens[j] + 1
                    pred[i] = j

            j -= 1

    def reconstruct(pred, start):
        i = start
        r = []
        while i and i > 0:
            r.append(s[i])
            i = pred[i]

        return list(reversed(r))

    # pretty pretty cool!
    print(s[1:])
    print(lens[1:])
    print(pred[1:])
    print('\n')
    print(reconstruct(pred, len(s) - 1))
    print(reconstruct(pred, len(s) - 2))


print(longest_tab(s))
print('\n')
print(longest_tab([10, 9, 2, 5, 3, 7, 101, 18]))
