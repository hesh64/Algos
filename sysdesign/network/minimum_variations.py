# todo there is a way to optimize this
# especially with the max(bag) min(bag)
def minimum_variation(throughput, threshold):
    bag = set()
    start = 0
    diff = 0
    for end in range(len(throughput)):
        bag.add(throughput[end])

        while start < end and max(bag) - min(bag) > threshold:
            bag.remove(throughput[start])
            start += 1
        diff = max(end - start + 1, diff)

    return diff


def main():
    throughput = [10, 1, 2, 4, 7, 2]
    threshold = 5
    print(minimum_variation(throughput, threshold))


main()
