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

    def combine(self, list1:Node, list2:Node):
        node1 = list1.head
        node2 = list2.head
        node3 = self.head
        while node1 and node2 is not None:
            self.insert(node1.data)
            self.insert(node2.data)
            node1 = node1.next
            node2 = node2.next
        if(node1 is None):
            while node2 is not None:
                self.insert(node2.data)
                node2 = node2.next
        elif(node2 is None):
            while node1 is not None:
                self.insert(node1.data)
                node1 = node1.next
        






list1 = SinglyLinkedList()  
list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(4)
list1.insert(5)

list2 = SinglyLinkedList()  
list2.insert(6)
list2.insert(7)
list2.insert(8)
list2.insert(9)
list2.insert(10)
list2.insert(11)

list3 = SinglyLinkedList()
list3.combine(list1,list2)

print("Initial lists:\n\nFirst:")
list1.out()
print("Second:")
list2.out()
print("\nMerged lists:")
list3.out()
print()



