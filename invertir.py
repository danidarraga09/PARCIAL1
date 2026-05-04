def reverseKGroup(head, k):

    current = head
    count = 0

    # verificar si existen k nodos
    while current and count < k:
        current = current.next
        count += 1

    if count < k:
        return head

    prev = None
    current = head
    count = 0

    # invertir k nodos
    while current and count < k:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        count += 1

    # conectar siguiente grupo
    head.next = reverseKGroup(current, k)

    return prev