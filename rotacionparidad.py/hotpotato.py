def hot_potato(head, t, q):
    cur = head
    while cur.next is not cur:
        for _ in range(t - 1):
            cur = cur.next
        cur.hits += 1
        if cur.hits == q:
            prev = cur
            while prev.next is not cur:
                prev = prev.next
            prev.next = cur.next
            cur = cur.next
        else:
            cur = cur.next
    return cur.val