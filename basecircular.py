class Node:
    def __init__(self,data):
     self.data=data
     self.next=None

class CircularLinkedList():
   def __init__(self):
      self.head=None

def first_insert(self,data):
   new_node=Node(data)
   self.head=new_node
   new_node.next=self.head

def insert_atbeginning(self,data):
   new_node=Node(data)
   if self.head is None:
      self.head=new_node
      new_node.next=self.head
      return
   current=self.head
   while current.next != self.head:
     current=current.next

   new_node.next=self.head
   self.head=new_node
   current.next=new.node
def insert_atend(self,data):
  new_node=Node(data)
  if self.head is None:
        self.head=new_node
        return
  current=self.head
  while current.next!=self.head:
     current=current.next
  new_node.next=self.head
  current.next=new_node
  
     


