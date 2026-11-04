class Stack:
    def __init__(self):
        self.items = []
 
    def push(self, x):
        self.items.append(x)
 
    def pop(self):
        return self.items.pop()
 
    def peek(self):
        return self.items[-1]
 
    def is_empty(self):
        return not self.items
def balanced(expr):
    pairs = {")": "(", "]": "[", "}": "{"}
    s = Stack()
    for ch in expr:
        if ch in "([{":
            s.push(ch)
        elif ch in pairs:
            if s.is_empty() or s.pop() != pairs[ch]:
                return False
    return s.is_empty()
 
 
print("2) '{[()]}' ->", balanced("{[()]}"), "| '{[(])}' ->", balanced("{[(])}"))
 