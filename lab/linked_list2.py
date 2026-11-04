class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class History:
    def __init__(self, page):
        self.cur = Node(page)

    def visit(self, page):
        n = Node(page)
        n.prev, self.cur.next = self.cur, n
        self.cur = n

    def back(self):
        if self.cur.prev:
            self.cur = self.cur.prev
        return self.cur.data

    def forward(self):
        if self.cur.next:
            self.cur = self.cur.next
        return self.cur.data


h = History("google.com")
h.visit("mongolia.gov.mn")
h.visit("news.mn")
print("2) Буцах:", h.back(), "| Дахин буцах:", h.back(), "| Урагш:", h.forward())