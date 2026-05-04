class Node:
    def __init__(self, val):
        self.val = val
        self.infected = False
        self.next = None

def is_prime(n):
    if n < 2: return False
    return all(n % i for i in range(2, int(n**0.5) + 1))

def infeccion(head, m):
    cur = head
    while cur.next is not cur:
        steps, count = 0, 1
        while count < m:
            cur = cur.next
            steps += 2 if cur.infected else 1
            count = steps + 1
        to_del = cur.next
        cur.next = to_del.next
        if is_prime(to_del.val):
            cur.next.infected = True
        cur = cur.next
    return cur.val