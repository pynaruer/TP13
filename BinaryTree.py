from Node import *


#DEF FONCTIONS

class BinaryTree():
    def __init__(self,root):
        self.__root = root

    def getRoot(self):
        return self.__root

    def isRoot(self, node):
        if self.__root == node:
            return True
        else:
            return False

    def size(self, node):
        if node is None:
            return 0
        else:
            return self.size(node.getLeft())+self.size(node.getRight())+1

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return self.printValues(node.getLeft())+self.printValues(node.getRight())+" "+str(node.getVal())

    def sumValues(self, node):
        if node is None:
            return 0
        else:
            return self.sumValues(node.getLeft())+node.getVal()+self.sumValues(node.getRight())

    def numberLeaves(self, node):
        if node is None:
            return 0
        elif node.getLeft() == None and node.getRight() == None:
            return 1
        else:
            return self.numberLeaves(node.getLeft())+self.numberLeaves(node.getRight())

    def numberInternalNodes(self, node):
        if node == None or (node.getLeft() == None and node.getRight() == None):
            return 0
        else:
            return self.numberInternalNodes(node.getLeft())+self.numberInternalNodes(node.getRight())+1

    def height(self, node):
         if node is None:
            return -1
         else :
            left = self.height(node.getLeft())
            right = self.height(node.getRight())
            return max(left, right) + 1

    def belongs(self, node, val):
        if node is None:
            return False
        if node.getVal() == val:
            return True
        else:
            return self.belongs(node.getRight(), val) or self.belongs(node.getLeft(), val)

    def ancestors(self, node, val):
        if node == None :
            return (val,"n'est pas dans cette arbre")
        else:
            if self.belongs(node.getLeft(), val):
                return str(node.getVal())+" "+str(self.ancestors(node.getLeft(), val))
            elif self.belongs(node.getRight(), val):
                return str(node.getVal())+" "+str(self.ancestors(node.getRight(), val))

    def descendants(self, node, val):
        if node == None:
            return (val,"n'est pas dans cette arbre")
        elif node.getVal() == val:
            return self.printValues(node.getLeft())+self.printValues(node.getRight())
        else:
            if self.belongs(node.getLeft(), val):
                return self.descendants(node.getLeft(), val)
            elif self.belongs(node.getRight(), val):
                return self.descendants(node.getRight(), val)

    def prefixe(self, node):
        if node == None:
            return ""
        else:
            return str(node.getVal())+" "+str(self.prefixe(node.getLeft()))+str(self.prefixe(node.getRight()))

    def infixe(self, node):
        if node == None:
            return ""
        else:
            return str(self.infixe(node.getLeft()))+str(node.getVal())+" "+str(self.infixe(node.getRight()))

    def postfixe(self, node):
        if node == None:
            return ""
        else:
            return str(self.postfixe(node.getLeft()))+str(self.postfixe(node.getRight()))+str(node.getVal()) + " "

    def listeTree(self, node):
        if node == None:
            return ""
        elif node.getLeft() == None and node.getRight() == None:
            return [node.getVal()]
        else:
            return [node.getVal(), (self.listeTree(node.getLeft())), self.listeTree(node.getRight())]


    def parcoursLargeur(self, node):
        list = self.listeTree(node)
        for elt in list:
            temp = ""
            if type(elt) == type(1):
                temp = temp+str(elt)+" "
            elif elt != None:
                for i in elt:
                    list.append(i)
        return temp


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
print("belong :",val," :",tree.belongs(tree.getRoot(),val))
print("ancestors ",val," : ", tree.ancestors(tree.getRoot(), val))
print("préfixe :", tree.prefixe(tree.getRoot()))
print("infixe :", tree.infixe(tree.getRoot()))
print("postfixe :", tree.postfixe(tree.getRoot()))
print("parcoursLargeur :", tree.parcoursLargeur(tree.getRoot()))
