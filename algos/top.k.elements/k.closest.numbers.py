from heapq import *


class ClosestTo:
    def __init__(self, val, x):
        self.val, self.x = val, x

    def __lt__(self, other):
        c = self.val - self.x
        o = other.val - other.x
        if c > 0:
            c = -c

        if o > 0:
            o = -o

        return c < o


def k_closest_numbers(nums, k, x):
    max_heap = []
    for num in nums:
        heappush(max_heap, ClosestTo(num, x))
        if len(max_heap) > k:
            heappop(max_heap)

    return [heappop(max_heap).val for i in range(len(max_heap))]


# this is one of those times where my solution was nothing like the right one.

"""
Utilizing a similar approach, we can find the numbers closest to ‘X’ through the following algorithm:

1. Since the array is sorted, we can first find the number closest to ‘X’ through Binary Search. Let’s say that number 
is ‘Y’.
2. The ‘K’ closest numbers to ‘Y’ will be adjacent to ‘Y’ in the array. We can search in both directions of ‘Y’ to find
the closest numbers.
3. We can use a heap to efficiently search for the closest numbers. We will take ‘K’ numbers in both directions of ‘Y’
and push them in a Min Heap sorted by their absolute difference from ‘X’. This will ensure that the numbers with the
smallest difference from ‘X’ (i.e., closest to ‘X’) can be extracted easily from the Min Heap.
4. Finally, we will extract the top ‘K’ numbers from the Min Heap to find the required numbers.
"""


# this is using a modified binary search approach. Because we returns the floor of the value in the array
# if the element is not found.

def just_another_binary_search(nums, k):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] < k:
            start = mid + 1

        elif nums[mid] > k:
            end = mid - 1
        else:
            return mid

    if start > 0:
        return start - 1
    return start


# Time complexity is O(k*log(k) + log(n))
# space O(k)
def k_closest_with_binary(nums, k, x):
    # O(log(n))
    index_of_val_or_ceiling = just_another_binary_search(nums, x)
    min_heap = []

    lower, upper = index_of_val_or_ceiling - 1, index_of_val_or_ceiling

    # O(k * log(k))
    for _ in range(k):
        if lower >= 0:
            heappush(min_heap, (nums[lower] - x, nums[lower]))
            lower -= 1
        if upper < len(nums):
            heappush(min_heap, (x - nums[upper], nums[upper]))
            upper += 1
        if len(min_heap) > k:
            heappop(min_heap)

    result = [heappop(min_heap)[1] for _ in range(k)]
    # O(k*log(k))
    result.sort()
    return result


"""
There is an even better solution
    
Alternate Solution using Two Pointers #
After finding the number closest to ‘X’ through Binary Search, we can use the Two Pointers approach to find the ‘K’ 
closest numbers. Let’s say the closest number is ‘Y’. We can have a left pointer to move back from ‘Y’ and a right 
pointer to move forward from ‘Y’. At any stage, whichever number pointed out by the left or the right pointer gives 
the smaller difference from ‘X’ will be added to our result list.

To keep the resultant list sorted we can use a Queue. So whenever we take the number pointed out by the left pointer,
we will append it at the beginning of the list and whenever we take the number pointed out by the right pointer we
will append it at the end of the list.
"""

from collections import deque


# time complexity O(log(n) + k) log(n) to search, k to iterate
# space O(k) queue size
def k_closest_with_two_pointers(nums, k, x):
    # O(log(n))
    index_of_val_or_floor = just_another_binary_search(nums, x)
    q = deque()
    lower, upper = index_of_val_or_floor - 1, index_of_val_or_floor + 1
    q.append(nums[index_of_val_or_floor])

    # O(k)
    for _ in range(k - 1):
        if lower >= 0 and upper < len(nums):
            if x - nums[lower] < nums[upper] - x:
                q.appendleft(nums[lower])
                lower -= 1
            else:
                q.append(nums[upper])
                upper += 1

        elif lower >= 0:
            q.appendleft(nums[lower])
            lower -= 1
        elif upper < len(nums):
            q.append(nums[upper])
            upper += 1

    return list(q)


def main():
    nums, k, x = [5, 6, 7, 8, 9], 3, 7
    result = k_closest_numbers(nums, k, x)
    print(result)

    nums, k, x = [5, 6, 7, 8, 9], 3, 7
    result = k_closest_with_binary(nums, k, x)
    print('modified binary', result)

    nums, k, x = [5, 6, 7, 8, 9], 3, 7
    result = k_closest_with_two_pointers(nums, k, x)
    print('two pointer', result)

    nums, k, x = [2, 4, 5, 6, 9], 3, 6
    result = k_closest_numbers(nums, k, x)
    print(result)

    nums, k, x = [2, 4, 5, 6, 9], 3, 6
    result = k_closest_numbers(nums, k, x)
    print('modified binary', result)

    nums, k, x = [2, 4, 5, 6, 9], 3, 6
    result = k_closest_with_two_pointers(nums, k, x)
    print('two pointer', result)

    nums, k, x = [2, 4, 5, 6, 9], 3, 10
    result = k_closest_numbers(nums, k, x)
    print(result)
    nums, k, x = [2, 4, 5, 6, 9], 3, 10
    result = k_closest_with_binary(nums, k, x)
    print('modified binary', result)
    nums, k, x = [2, 4, 5, 6, 9], 3, 10
    result = k_closest_with_two_pointers(nums, k, x)
    print('two pointer', result)


main()
