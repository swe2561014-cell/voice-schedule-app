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
 
text, undo = "", Stack()
for word in ["Сайн ", "байна ", "уу"]:
    undo.push(text)
    text += word
print("1) Текст:", repr(text))
text = undo.pop()
print("   Undo хийсний дараа:", repr(text))
 