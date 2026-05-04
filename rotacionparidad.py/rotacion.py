def rotacion_paridad(head, m):
    cur = head
    while cur.next is not cur:
        for _ in range(m - 2):
            cur = cur.next
        to_del = cur.next
        cur.next = to_del.next
        m = m + 1 if to_del.val % 2 == 0 else max(2, m - 1)
        cur = cur.next
    return cur.val