class Node():
    def __init__(self, data):
        self.data = data
        self.next = None  

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head is None: 
            self.head = node 
            return
        last = self.head 
        while (last.next): 
            last = last.next
        last.next =  node 

    def out(self):
        if self.head == None: return print("List is empty!")
        node = self.head
        while node is not None:
            print(node.data, end = " ")
            node = node.next
        print()


class Tree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self, count):
        if self.left:
            self.left.printTree(count+5)
        for i in range (0,count):
            print(" ", end="")
        print(self.data)
        if self.right:
            self.right.printTree(count+5)


def TreeToList(tree, list):
    if tree.left:
        TreeToList(tree.left, list)
    list.insert(tree.data)
    if tree.right:
        TreeToList(tree.right, list)


myTree = Tree(10)
myTree.insert(11)
myTree.insert(1)
myTree.insert(5)
myTree.insert(15)
myTree.insert(4)

myList = SinglyLinkedList()
TreeToList(myTree,myList)

print("Binary tree (Tilt your head to the left):\n")
myTree.printTree(0)
print("\nSorted singly linked list derived from a binary tree:")
myList.out()
print()