class BrowseRatings:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def is_empty(self):
        return len(self.max_stack) == 0 and len(self.main_stack) == 0

    def push(self, val):
        if self.is_empty():
            self.main_stack.append(val)
            self.max_stack.append(val)
        else:
            self.main_stack.append(val)
            if val > self.max_stack[-1]:
                self.max_stack.append(val)
            else:
                self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if self.main_stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()

        return self.main_stack.pop()

    def max_rating(self):
        if len(self.max_stack) > 0:
            return self.max_stack[-1]


def main():
    ratings = BrowseRatings()
    ratings.push(5)
    ratings.push(0)
    ratings.push(2)
    ratings.push(4)
    ratings.push(6)
    ratings.push(3)
    ratings.push(10)

    print(ratings.main_stack)
    print("Maximum Rating: " + str(ratings.max_rating()))

    ratings.pop()  # Back button effect
    print("\nAfter clicking back button\n")
    print(ratings.main_stack)
    print("Maximum value: " + str(ratings.max_rating()))


main()
