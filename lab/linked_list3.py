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

    def to_list(self):
        out, p = [], self.head
        while p:
            out.append(p.data)
            p = p.next
        return out


blocks = LinkedList()
for size in [64, 128, 256]:
    blocks.append(f"{size}KB")
print("3) Чөлөөт блокууд:", blocks.to_list())