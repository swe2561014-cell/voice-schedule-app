class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = n

    def insert_after(self, node, data):
        n = Node(data)
        n.next = node.next
        node.next = n

    def to_list(self):
        out, p = [], self.head
        while p:
            out.append(p.data)
            p = p.next
        return out


songs = LinkedList()
for s in ["Дуу A", "Дуу B", "Дуу C"]:
    songs.append(s)
songs.insert_after(songs.head, "Шинэ дуу")
print("1) Жагсаалт:", songs.to_list())