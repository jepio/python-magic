Binary Tree
===========

The binary tree is an interesting data structure. I have built my own and am planning on checking out other interesting data structures in this repository.

To use this class import the class and create a head Node object:
```python
from btree import Node

tree = Node(5)
tree.insert(10)
tree.insert(3)

print tree
```

Currently I have implemented searching for a value in the tree, inserting a value into the tree, searching for an ancestor node and printing the tree.

In [test_btree.py](test_btree.py) you will find `py.test` unit tests, of which the implementation passes all. 

