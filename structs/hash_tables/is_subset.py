"""Implement the is_subset(list1,list2) function which will take two lists as input and check
whether one list is the subset of the other. This method is already available in Python, but
we’ll be implementing it using hash tables.
"""


# O(m + n) m = len(l1) n = len(l2)
def is_subset(l1, l2):
    d = {}

    for i in l1:
        d[i] = True

    for j in l2:
        if j not in d:
            return False

    return True


"""You have to implement the is_disjoint() function which checks whether 
two given lists are disjoint or not. Two lists are disjoint if there are no common 
elements between them. The assumption is that there are no duplicate elements in each list."""


# O(m + n) m = len(l1) n = len(l2)
def is_disjoint(l1, l2):
    d = {}
    for i in l1:
        d[i] = True

    for j in l2:
        if j in d:
            return False

    return True


"""By definition, (a, b) and (c, d) are symmetric pairs iff, a = d and b = c. In this problem, 
you have to implement the find_symmetric(list) function which will find all the symmetric pairs 
in a given list.
"""


# O(n) time and space
def is_symmetric(l):
    hash_ = set()
    pairs = []
    for x, y in l:
        skey = f'{y},{x}'
        # look ups are o(1) avg
        if skey in hash_:
            pairs.append([x, y])
            pairs.append([y, x])
        else:
            hash_.add(f'{x},{y}')

    return pairs


"""You have to implement the trace_path() function which will take in a list of source-destination pairs and return 
the correct sequence of the whole journey from the first city to the last."""


# O(n) where n is len(my_dict)
def trace_path(my_dict):  # A Map object
    keys = set(my_dict.keys())
    city = (keys - set(my_dict.values())).pop()
    cities = []

    while city in my_dict:
        d = my_dict[city]
        cities.append([city, d])
        city = d
    return cities


"""
Problem Statement #
In this problem, you have to implement the find_pair() function which will
 find two pairs, [a, b] and [c, d], in a list such that :

a+b = c+da+b=c+d

You only have to find the first two pairs in the list which satisfies the above condition.

"""


# you can solve this with a dict lookup
# at a more efficient time.
# for the key store the sum of the two values, and for the value
# sotre the two values, then the next time you run into that value
#  check if the key exists and if the two values are different
# Time O(n^2)
def find_pair(my_list):
    added = {}

    for i in range(len(my_list)):
        for j in range(len(my_list)):
            if i != j:
                big, sma = max(my_list[i], my_list[j]), min(my_list[i], my_list[j])
                summed = big + sma
                if summed not in added:
                    added[summed] = set()
                added[summed].add((sma, big))
                if len(added[summed]) > 1:
                    return [[x, y] for x, y in added[summed]]


"""You have to implement the is_formation_possible() function which will find whether 
a given word can be formed by combining two words from a dictionary. We assume that all 
words are in lower case.
"""


# O(n + k^2)
def is_formation_possible(lst, word):
    if len(lst) < 2 or len(word) < 2:
        return False

    # O(n) where n is length of list of words
    words = set(lst)
    start = 0
    # O(k) where k is the number of letters in the phrase
    end = 1
    while end <= len(word):
        # slicing the string is O(k) alone
        if word[start: end] in words:
            start = end
            break
        end += 1

    if word[start: len(word)] in words:
        return True

    return False


"""In this problem, you have to implement the findSum(lst,k) function which will take a number k as input and return
 two numbers that add up to k."""


# O(n)
def findSum(lst, k):
    seen = {}
    for ele in lst:
        if (k - ele) in lst:
            return [ele, k - ele]

        seen[k - ele] = ele
    return [-1, -1]


"""Implement a function, findFirstUnique(lst) that returns the first unique integer in the list"""


# O(n)
def find_first_unique(lst):
    seen = {}
    for ele in lst:
        if ele not in seen:
            seen[ele] = 0
        seen[ele] += 1

    for ele in lst:
        if seen[ele] == 1:
            return ele

    return -1


def main():
    input = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]
    result = is_symmetric(input)
    print(result)

    lst = ["the", "hello", "there", "answer", "any",
           "by", "world", "their", "abc"]
    word = "helloworld"
    result = is_formation_possible(lst, word)
    print(f'can {word} be constructed from the words in: {lst}? {result}')


main()
