# tests
from tree import Tree
from node import Node

tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)



def test_find_added():
    assert tree.find(3)
    assert tree.find(4)
    assert tree.find(0)
    assert tree.find(8)
    assert tree.find(2)

def test_find_not_added():
    assert not tree.find(5)
    assert not tree.find(1)
    assert not tree.find(6)
    assert not tree.find(7)
    assert not tree.find(9)