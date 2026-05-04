def puertas_reversa(head, m, a):
    cur = head
    direction = 1  # 1 adelante, -1 atrás

    def advance(node, steps):
        # En lista simple, "atrás" = dar n-1 pasos adelante
        if direction == 1:
            for _ in range(steps):
                node = node.next
        else:
            size = 0
            tmp = node
            while True:
                tmp = tmp.next
                size += 1
                if tmp is node:
                    break
            for _ in range(size - steps):
                node = node.next
        return node

    while cur.next is not cur:
        cur = advance(cur, m - 2)
        to_del = cur.next
        cur.next = to_del.next
        if to_del.val % a == 0:
            direction *= -1
        cur = cur.next

    return cur.val