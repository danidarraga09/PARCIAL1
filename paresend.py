def even_to_end(head):
    if not head:
        return None
    odd = odd_tail = head
    even = even_head = head.next
    cur = even

    while cur and cur.next:
        odd_tail.next = cur.next
        odd_tail = odd_tail.next
        cur.next = cur.next.next
        cur = cur.next

    odd_tail.next = even_head
    return odd