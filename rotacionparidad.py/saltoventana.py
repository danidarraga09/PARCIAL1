def saltos_ventana(head, m, w):
    cur = head
    while cur.next is not cur:
        for _ in range(m - 2):
            cur = cur.next
        to_del = cur.next
        cur.next = to_del.next
        for _ in range(w):
            cur = cur.next
    return cur.val