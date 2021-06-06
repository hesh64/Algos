def parent(i):
    """
    Calcuate the parent index
    :param i:
    :return:
    """
    if i == 1:
        return -1

    return i // 2


def child(i):
    """
    calculate the left child
    :param i:
    :return:
    """
    return 2 * i


# logn
def bubble_up(h, i):
    """
    if i is smaller than it's parent, then swap them, then repeat
    :param h:
    :param i:
    :return:
    """
    if parent(i) == -1:
        return

    if h.array[parent(i)] > h.array[i]:
        h.array[parent(i)], h.array[i] = h.array[i], h.array[parent(i)]
        bubble_up(h, parent(i))


# logn
def bubble_down(h, i):
    c = child(i)
    min_index = i
    if c <= h.cap and h.array[c] < h.array[min_index]:
        min_index = c

    if c + 1 <= h.cap and h.array[c + 1] < h.array[min_index]:
        min_index = c + 1

    if min_index != i:
        h.array[i], h.array[min_index] = h.array[min_index], h.array[i]
        bubble_down(h, min_index)


def make_heap(arr):
    """
    static method to construct a heap from an array
    :param arr:
    :return:
    """
    h = Heap(len(arr))

    for n in arr:
        h.push(n)

    return h


# n
def heapify(arr):
    h = Heap(len(arr))
    h.array[1:] = arr
    h.cap = len(h.array) - 1

    half = len(h.array) // 2
    for i in range(half, 0, -1):
        bubble_down(h, i)

    return h


def check_if_kth_smallest_is_lt(h, k, x):
    """
    we want to check if the kth smallest/largest element in the heap is less than x

    if we visit k nodes that are less than x then that's true

    to avoid traversing the full heap, we -1 every time we find a node until our count is 0 then we
    trigger our base case
    and only go down to the children of a node that was also < x
    :param h:
    :param k:
    :param x:
    :return:
    """

    # O(k)
    def compare_heap(h, i, count, x):
        if count <= 0 or i > h.cap:
            return count

        if h.array[i] < x:
            count = compare_heap(h, child(i), count - 1, x)
            count = compare_heap(h, child(i) + 1, count, x)

        return count

    return compare_heap(h, 1, k, x) == 0


class Heap:
    def __init__(self, size):
        self.cap = 0
        self.array = [None] * (size + 1)

    def insert(self, item):
        if len(self.array) == self.cap + 1:
            raise Exception('heap is full')

        self.cap += 1
        self.array[self.cap] = item
        bubble_up(self, self.cap)

    def pop(self):
        if self.cap <= 0:
            raise Exception('heap is empty')

        val = self.array[1]
        self.array[1] = self.array[self.cap]
        self.cap -= 1
        bubble_down(self, 1)
        return val


a = [91, 16, 71, 1623, 12, 1, 8, 72, 6]
h = make_heap(a)
for _ in range(len(a)):
    print(h.pop())

a = [91, 16, 71, 1623, 12, 1, 8, 72, 6]
h = heapify(a)
for _ in range(len(a)):
    print(h.pop())

a = [91, 16, 71, 1623, 12, 1, 8, 72, 6]
h = heapify(a)
print(check_if_kth_smallest_is_lt(h, 3, 9))
