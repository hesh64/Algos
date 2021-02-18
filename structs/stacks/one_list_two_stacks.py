class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.stack = []
        self.depth_1 = 0
        self.depth_2 = 0

    # Insert Value in First Stack
    def push1(self, value):
        self.stack.insert(0, value)
        self.depth_1 += 1

    # Insert Value in Second Stack
    def push2(self, value):
        self.stack.append(value)
        self.depth_2 += 1

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.depth_1 > 0:
            return self.stack.pop(0)

        return None

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.depth_2 > 0:
            return self.stack.pop()
        return None
