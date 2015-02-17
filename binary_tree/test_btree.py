from btree import ancestor, Node

tree = Node(30).insert(52).insert(8).insert(3).insert(20).insert(10).insert(29)
print tree

def make_test(a, b, c):
    def _test():
        assert ancestor(tree, a, b) == c
    return _test

cases = [(8, 52, 30),
         (3, 52, 30),
         (20, 52, 30),
         (10, 52, 30),
         (29, 52, 30),
         (3, 20, 8),
         (10, 29, 20),
         (3, 8, 8),
         (10, 20, 20),
         (20, 29, 20),
         (20, 3, 8),
         (3, 3, 3)]

dict_ = globals()
for num, case in enumerate(cases):
    dict_["test_%d" % num] = make_test(*case)
