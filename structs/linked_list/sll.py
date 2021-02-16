class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    # Time O(1)
    def get_head(self):
        return self.head_node

    # Time O(1)
    def is_empty(self):
        return self.head_node is None

    # Time O(1)
    def insert_at_head(self, data):
        new_head = Node(data)
        new_head.next_element = self.head_node
        self.head_node = new_head
        return self.head_node

    # Time O(n) where n is length of list.
    def insert_at_tail(self, data):
        if self.is_empty():
            self.insert_at_head(data)
            return

        temp = self.get_head()
        while temp.next_element is not None:
            temp = temp.next_element

        temp.next_element = Node(data)

    # Time O(k) where 0 <= k < n
    def insert_at_kth(self, k, data):
        if self.is_empty():
            return False

        counter = 1
        cur = self.get_head()

        while cur.next_element is not None and counter < k:
            counter += 1
            cur = cur.next_element

        node = Node(data)
        node.next_element = cur.next_element
        cur.next_element = node

        return True

    # Time: Best case O(1) Worst O(n) avg O(n/2) => O(n)
    # Space: O(1)
    def search_itr(self, data):
        if self.is_empty():
            return False

        cur = self.get_head()

        while cur is not None:
            if cur.data == data:
                return True

            cur = cur.next_element

        return False

    # Time: Best case O(1) Worst O(n) avg O(n/2) => O(n)
    # Space: O(1) best O(n) worst / avg
    def search_rec(self, data):
        def _search_rec(head, _data):
            if head is None:
                return False

            if head.data == _data:
                return True

            return _search_rec(head.next_element, _data)

        return _search_rec(self.get_head(), data)

    # time O(1)
    def delete_at_head(self):
        if self.is_empty():
            return False

        self.head_node = self.head_node.next_element
        return True

    # time O(k) where 0 <= k < n
    def delete_at_kth(self, k):
        if self.is_empty():
            return False

        count = 1
        cur = self.get_head()

        while cur.next_element and count < k:
            cur = cur.next_element
            count += 1

        cur.next_element = None
        return True

    # this is a search, then a deletion so O(n)
    def delete(self, data):
        if self.is_empty():
            return False

        cur = self.get_head()
        if cur.data == data:
            self.delete_at_head()
            return True

        while cur.next_element and cur.next_element.data != data:
            cur = cur.next_element

        if cur.next_element and cur.next_element.data == data:
            cur.next_element = cur.next_element.next_element

            return True

        return False

    # Time O(k)
    def delete_at_tail(self):
        if self.is_empty():
            return False

        head = self.get_head()
        if head.next_element is None:
            self.head_node = None

        cur = head
        while cur.next_element is not None and cur.next_element.next_element:
            cur = cur.next_element

        cur.next_element = None

        return True

    def print_list(self):
        if self.is_empty():
            print("list is empty")
            return False

        temp = self.head_node

        while temp.next_element is not None:
            print(temp.data, end=' -> ')
            temp = temp.next_element

        print(temp.data, '-> None')
        return True


def main():
    lst = LinkedList()
    for i in range(1, 10):
        lst.insert_at_head(i)

    lst.print_list()

    lst = LinkedList()
    for i in range(1, 10):
        lst.insert_at_tail(i)

    lst.print_list()

    print(lst.search_itr(7))
    print(lst.search_rec(7))

    lst.print_list()
    lst.delete(7)
    lst.print_list()


main()
