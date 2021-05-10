import heapq
import random

random.seed('42')
# reenable this line
# lists = [sorted([random.randint(1, 10 ** 14) for _ in range(random.randint(500, 1000))]) for _ in range(500)]
# comment the bottom line
lists = [sorted([random.randint(1, 10 ** 14) for _ in range(random.randint(5, 10))]) for _ in range(5)]

print(len(lists), sum([len(l) for l in lists]))
print(lists[0][10:100])


def merge_lists(lists):
    h = [(l[0], 0, i) for i, l in enumerate(lists)]
    heapq.heapify(h)

    file = []
    while h:
        value, index, list_index = heapq.heappop(h)
        file.append(value)
        if index < len(lists[list_index]) - 1:
            heapq.heappush(h, (lists[list_index][index + 1], index + 1, list_index))

    return file


file = merge_lists(lists)
print(len(file))
print(all(file[i - 1] < file[i] for i in range(1, len(file))))

nums = [3, -1, 2, 6, 4, 5, 8]


# O(nlgk)
def sort_almost_sorted_array(nums, k):
    h, i = [], 0
    for n in nums:
        heapq.heappush(h, n)
        while len(h) >= k:
            nums[i] = heapq.heappop(h)
            i += 1

    while h:
        nums[i] = heapq.heappop(h)
        i += 1


sort_almost_sorted_array(nums, 2)
print(nums)
