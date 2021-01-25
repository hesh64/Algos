nodes = [('animal', 'mammal'),
         ('animal', 'bird'),
         ('lifeform', 'animal'),
         ('cat', 'lion'),
         ('mammal', 'cat'),
         ('animal', 'fish')]


# just your friendly neighborhood node
class Node:
    def __init__(self, val, children=[]):
        # holds a value
        self.val = val
        # holds children
        self.children = children


# print a tree that came in as a stream
def print_tree(stream):
    # how many times has v be a value?
    # we only need this to get the one key that was never
    # used as a value aka our head
    value_freq = {}
    # what are the heads children names/vals?
    children = {}
    # store value_freq, and children as frequency
    for (k, v) in stream:
        if k not in children:
            # a list maintains order
            children[k] = []
        children[k].append(v)

        if k not in value_freq:
            value_freq[k] = 0

        if v not in value_freq:
            value_freq[v] = 0
        value_freq[v] += 1

        if v not in children:
            children[v] = []

    # where is my head?
    head = None
    for (k, v) in value_freq.items():
        if v == 0:
            # there it is
            head = k

    # pass in a string for head
    # and children is an object
    def attach_children(head, children):
        # pass you a head val as a stirng, look it up in children
        # initialize your children and then return
        if head in children:
            node = Node(head, children[head])
            # if it's empty this won't run so we are all good.
            node.children = [attach_children(child, children) for child in node.children]
            return node

    # build the tree
    tree = attach_children(head, children)
    # print(tree.children)

    def _print(tree, tabs=0):
        if tree:
            print(' ' * tabs, tree.val)
            [_print(c, tabs + 2) for c in tree.children]

    return _print(tree)


def main():
    print_tree(nodes)


main()
