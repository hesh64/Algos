"""
Given an array with positive numbers and a target number, find all of its
contiguous subarrays whose product is less than the target number.
"""

# O(n^3) -> for loop while loop then copying over the array.
# space O(n^3)
def subarray_less_than_product_with_target(arr, target):
    result, start, mult = [], 0, 1

    for end in range(len(arr)):
        mult = 1
        start = end

        while start >= 0 and mult < target:
            mult *= arr[start]
            if mult < target:
                result.append(arr[start: end + 1])

            start -= 1

    return result


def main():
    print(subarray_less_than_product_with_target([2, 5, 3, 10], 30))
    print(subarray_less_than_product_with_target([8, 2, 6, 5], 50))


main()
