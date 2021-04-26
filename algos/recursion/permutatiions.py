def find_all_permutations(arr):
    perms = []

    def helper(arr, i, perms):
        if i == len(arr) - 1:
            perms.append(arr[:])

        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            helper(arr, i + 1, perms)
            arr[i], arr[j] = arr[j], arr[i]

    helper(arr, 0, perms)
    return perms


def main():
    print(find_all_permutations([1, 2, 3]))


main()
