class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)

        if not self.head:
            self.head = new
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new


def merge(l1, l2):

    dummy = Node(0)
    current = dummy

    while l1 and l2:

        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    current.next = l1 or l2

    return dummy.next


# CREAR LISTAS
lista1 = LinkedList()
lista2 = LinkedList()

for i in [1, 3, 5, 7]:
    lista1.insert(i)

for i in [2, 4, 6, 8]:
    lista2.insert(i)

# FUSIONAR
result = merge(lista1.head, lista2.head)

# MOSTRAR
while result:
    print(result.data, end=" -> ")
    result = result.next

print("None")