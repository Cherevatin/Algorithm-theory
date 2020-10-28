class Node():
    def __init__(self, data):
        self.data = data
        self.next = None  

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):  ## вставка в начало
        node = Node(data)
        node.next = self.head
        self.head = node

    def out(self):
        if self.head == None: return print("List is empty!")
        node = self.head
        while node is not None:
            print(node.data, end = " ")
            node = node.next
        print()

    def reverseList(self):
        if self.head == None: return print("List is empty!")
        prev = None
        n = self.head
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        self.head = prev


link_list = SinglyLinkedList()  
link_list.insert(5)
link_list.insert(4)
link_list.insert(3)
link_list.insert(2)
link_list.insert(1)

print("Initial list:")
link_list.out()

print("Reversed list:")
link_list.reverseList()
link_list.out()
