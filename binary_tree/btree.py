""" Self written binary tree. """


def ancestor(tree, a, b):
    """ Find the value of the lowest common ancestor of `a` and `b`. """
    a, b = sorted((a, b))
    return tree.ancestor(a, b).value


class Node(object):
    """
    A node of a binary tree.
    """

    def __init__(self, value):
        """ Create a node with a value. """
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        """ Insert a value into the tree, search for where to put the node. """
        if value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        return self

    def find(self, value):
        """ Return the value if it exists in the tree, else None. """
        if value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        elif value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        else:
            return self

    def ancestor(self, a, b):
        """ Return the lowest common ancestor of nodes with values a, b. """
        if self.value > a and self.value > b:
            return self.left.ancestor(a, b)
        elif self.value >= a and self.value <= b:
            return self
        else:
            return self.right.ancestor(a, b)

    def __repr__(self):
        """ String representation of the tree. """
        string = []
        if self.left:
            string += [repr(self.left)]
        string += [str(self.value)]
        if self.right:
            string += [repr(self.right)]
        return ','.join(string)

