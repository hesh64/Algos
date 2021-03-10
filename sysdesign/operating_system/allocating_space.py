def allocated_space(array, size):
    spots = []
    start = 0
    summed = 0
    for end in range(len(array)):
        summed += array[end]
        if summed == size:
            spots.append([start, end + 1])

        while start < end and summed > size:
            summed -= array[start]
            start += 1
            if summed == size:
                spots.append([start, end + 1])

    return len(spots)


def main():
    array = [3, 4, 7, 2, 3, 1, 4, 2]
    process = 7
    print(allocated_space(array, process))
    array = [1, 2, 3, 4, 5, 6, 7, 1, 23, 21, 3, 1, 2, 1, 1, 1, 1, 1, 12, 2, 3, 2, 3, 2, 2]
    process = 1
    print(allocated_space(array, process))


main()
