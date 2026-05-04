def zigzag(head):
    cur = head
    while cur and cur.next and cur.next.next:
        a, b, c = cur, cur.next, cur.next.next
        cur.next = c
        b.next  = c.next
        c.next  = b
        cur = b
    return head