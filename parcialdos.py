class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Insert_atbeginnig(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def Insert_atend(self, data):
        new_node = Node(data)

        if self.head == None:
         self.head= new_node
         return
        
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
    
    def display(self):
        current=self.head
        while current.next is not None:
            print(current.data,end="-->")
            current= current.next
        
        print("None")
        
    def search(self,target):
        current=self.head
        while current is not None:
            if current.data==target:
                print("Encontrado")
            current=current.next
        print("no encontrado")
        
    def deletefirst(self):
        if self.head is not None:
            self.head=self.head.next
            



