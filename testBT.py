from BinaryTree import *
from Node import *

#PRINCIPAL

tree = BinaryTree(Node(12))

tree.getRoot().setLeft(Node(5))
tree.getRoot().getLeft().setLeft(Node(4))
tree.getRoot().getLeft().setRight(Node(6))
tree.getRoot().getLeft().getLeft().setLeft(Node(3))

tree.getRoot().setRight(Node(17))
tree.getRoot().getRight().setRight(Node(19))
tree.getRoot().getRight().getRight().setLeft(Node(18))
tree.getRoot().getRight().getRight().setRight(Node(21))

print("size:",tree.size(tree.getRoot()))
print("print values :",tree.printValues(tree.getRoot()))
print("sum values :",tree.sumValues(tree.getRoot()))
print("number leaves :",tree.numberLeaves(tree.getRoot()))
print("number internal nodes:",tree.numberInternalNodes(tree.getRoot()))
print("height :",tree.height(tree.getRoot()))
val = 1
print("belong :",val," :",tree.belongs(tree.getRoot(), val))
print("ancestors ",val," : ", tree.ancestors(tree.getRoot(), val))
print("préfixe :", tree.prefixe(tree.getRoot()))
print("infixe :", tree.infixe(tree.getRoot()))
print("postfixe :", tree.postfixe(tree.getRoot()))
print("parcoursLargeur :", tree.parcoursLargeur(tree.getRoot()))
