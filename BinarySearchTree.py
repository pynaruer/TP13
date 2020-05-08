from BinaryTree import *
from Node import *


#DEF FONCTIONS

class BinarySearchTree(BinaryTree):

    def __init__(self, root):
        BinaryTree.__init__(self, root)

    def contains(self, node, value):
        if node is None:
            return 0
        elif node.getVal() == value and self.isRoot(node):
            return True
        elif node.getVal() == value:
            return 1
        else:
            return (self.contains(node.getLeft(), value)+self.contains(node.getRight(), value)) > 0

    def findMin(self, node):
        return min((self.infixe(node)).split())
