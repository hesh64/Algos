from collections import deque

"""
Problem Statement #
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example,
 {1, 2, 3} has the following six permutations:

"""


# Time O(n * n!)
# Space O(n * n!)
def find_permutations(nums):
    length = len(nums)
    results = []
    permutations = deque()

    permutations.append([])

    for num in nums:
        size = len(permutations)
        for _ in range(size):
            old = permutations.popleft()

            for j in range(len(old) + 1):
                new_perm = list(old)
                new_perm.insert(j, num)

                if len(new_perm) == length:
                    results.append(new_perm)
                else:
                    permutations.append(new_perm)

    return results


"""
String Permutations by changing case (medium)

Given a string, find all of its permutations preserving the character 
sequence but changing case.
"""


# Time O(n * 2^n)
# Space O(n * 2^n)
def find_letter_case_string_permutations(string):
    permutations = []
    permutations.append(string)

    for i in range(len(string)):
        if string[i].isalpha():
            size = len(permutations)
            for j in range(size):
                chs = list(permutations[j])

                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))

    return permutations


"""
Balanced Parentheses (hard)
For a given number ‘N’, write a function to generate all combination of 
‘N’ pairs of balanced parentheses.


"""


def main():
    result = find_permutations([1, 3, 5])
    print(result)

    result = find_letter_case_string_permutations("ad52")
    print(result)


main()
