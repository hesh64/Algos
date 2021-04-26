class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if (self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def print_list(self):
        if (self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if (first_element is not None):
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    def delete(self, value):
        deleted = False
        if self.is_empty():  # Check if list is empty -> Return False
            print("List is Empty")
            return deleted
        current_node = self.get_head()  # Get current node
        previous_node = None  # Get previous node
        if current_node.data is value:
            self.delete_at_head()  # Use the previous function
            deleted = True
            return deleted

        # Traversing/Searching for Node to Delete
        while current_node is not None:
            # Node to delete is found
            if value is current_node.data:
                # previous node now points to next node
                previous_node.next_element = current_node.next_element
                current_node.next_element = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next_element

        return deleted

    def search(self, dt):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head_node
        while (temp is not None):
            if (temp.data is dt):
                return temp
            temp = temp.next_element

        print(dt, " is not in List!")
        return None

    def length(self):
        # start from the first element
        curr = self.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length


"""By definition, a loop is formed when a node in your linked list points to a previously
 traversed node.

You must implement the detect_loop() function which will take a linked list as input and
 deduce whether or not a loop is present.

You have already seen this challenge previously in chapter 3 of this course. Here you
 would use HashTables for a more efficient solution.

"""


# dict lookups can increase to O(n) is the worst case, so
# this can be O(n^2)
def detect_loop(lst):
    seen = {}

    cur = lst.get_head()
    while cur:
        if cur.data not in seen:
            seen[cur.data] = True
        else:
            return True

        cur = cur.next_element

    return False


"""You will now be implementing the remove_duplicates() function. When a linked
 list is passed to this function, it removes any node which is a duplicate of another existing node.

You have already seen this challenge previously in chapter 3 of this course.
Here you would use HashTables for a more efficient solution.

"""


# O(n) on average where n is the length of the list
# but can increase to O(n^2) dur to dict lookup in the case where
# there are no duplicates at all
def remove_duplicates(ll):
    seen = {}
    cur = ll.get_head()

    while cur:
        if cur.next_element and cur.next_element.data in seen:
            cur.next_element = cur.next_element.next_element
        else:
            seen[cur.data] = True
        cur = cur.next_element
    return


def main():
    ll = LinkedList()
    ll.insert_at_head(7)
    head = ll.get_head()
    head.next_element = Node(14)
    head.next_element.next_element = Node(21)
    head.next_element.next_element.next_element = head

    result = detect_loop(ll)
    print(result)

    ll = LinkedList()
    ll.insert_at_head(7)
    head = ll.get_head()
    head.next_element = Node(14)
    head.next_element.next_element = Node(21)
    head.next_element.next_element.next_element = Node(14)
    head.next_element.next_element.next_element.next_element = Node(22)
    head.next_element.next_element.next_element.next_element.next_element = Node(7)
    ll.print_list()
    remove_duplicates(ll)
    ll.print_list()


main()
