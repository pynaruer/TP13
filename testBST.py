from BinarySearchTree import *

#PRINCIPAL

tree = BinarySearchTree(Node(4))

tree.getRoot().setLeft(Node(2))
tree.getRoot().getLeft().setLeft(Node(0))
tree.getRoot().getLeft().setRight(Node(3))
tree.getRoot().getLeft().getLeft().setRight(Node(1))

tree.getRoot().setRight(Node(20))
tree.getRoot().getRight().setLeft(Node(12))
tree.getRoot().getRight().getLeft().setLeft(Node(7))
tree.getRoot().getRight().getLeft().getLeft().setLeft(Node(6))
tree.getRoot().getRight().getLeft().setRight(Node(15))
tree.getRoot().getRight().getLeft().getRight().setLeft(Node(13))
tree.getRoot().getRight().getLeft().getRight().getLeft().setRight(Node(14))

val = 1
print("contains :",val," : ",tree.contains(tree.getRoot(), val))
print("findMin :",tree.findMin(tree.getRoot()))


