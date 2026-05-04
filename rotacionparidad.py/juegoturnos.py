class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None

def juego(head, rondas):
    cur = head
    for _ in range(rondas):
        if cur.next is cur:
            break
        # El jugador pierde si su score es el menor entre él y el siguiente
        if cur.score < cur.next.score:
            print(f"{cur.name} eliminado (score {cur.score})")
            prev = cur
            while prev.next is not cur:
                prev = prev.next
            prev.next = cur.next
            cur = cur.next
        else:
            cur.score += 1  # gana, acumula punto
            cur = cur.next

    return cur.name  # ganador