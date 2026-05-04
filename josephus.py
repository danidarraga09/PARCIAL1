def josephus(n, m, k):
    # Construir lista circular
    head = Node(1)
    cur = head
    for i in range(2, n + 1):
        cur.next = Node(i)
        cur = cur.next
    cur.next = head

    cur = head
    while cur.next is not cur:
        for _ in range(m - 2):
            cur = cur.next
        to_del = cur.next
        cur.next = to_del.next
        if to_del.val % k == 0:
            cur.next = cur.next.next
        cur = cur.next

    return cur.val
