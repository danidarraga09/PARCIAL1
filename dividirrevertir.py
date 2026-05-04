def split_and_reverse(head):
    # Encontrar mitad con slow/fast
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Cortar y revertir segunda mitad
    second = slow.next
    slow.next = None
    prev = None
    while second:
        second.next, prev, second = prev, second, second.next

    return head, prev