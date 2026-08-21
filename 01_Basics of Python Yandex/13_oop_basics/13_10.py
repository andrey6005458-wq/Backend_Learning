class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0

stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")