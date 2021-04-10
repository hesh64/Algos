# def find_substring(string, pattern):
#     p1, p2, start = 0, 0, 0
#
#     s, e = 0, len(string) - 1
#     while p1 < len(string):
#         if p2 < len(pattern) and string[p1] == pattern[p2]:
#             p2 += 1
#             if p2 == len(pattern):
#                 start = p1
#                 p2 -= 1
#                 while start > 0 and p2 > 0:
#                     if string[start] == pattern[p2]:
#                         p2 -= 1
#                     start -= 1
#                 if p1 - start + 1 < e - s + 1:
#                     s, e = start, p1
#         p1 += 1
#     if e - s + 1 == len(string):
#         return '_'
#     return string[s: e + 1]
#
#
# print(find_substring('aabdec', 'abc'))
# print(find_substring('abdbca', 'abc')) 
# print(find_substring('adcad', 'abc'))
# #
intr = [[1, 3], [2, 1]]
B = ([(left, +1) for left, _ in intr] + [(right, - 1) for _, right in intr])
print(B)