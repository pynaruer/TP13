from Node import *

class BinaryTree :
    def __init__(self,root):
        self.__root = root
    def getRoot(self):
        return self.__root

Node3 = Node(3,None,None)
Node4 = Node(4,Node3,None)
Node6 = Node(6,None,None)
Node5 = Node(5,Node4,Node6)

Node18 = Node(18,None,None)
Node21 = Node(21,None,None)
Node19 = Node(19,Node18,Node21)
Node17 = Node(17,None,Node19)

Node12 = Node(12,Node5,Node17)
