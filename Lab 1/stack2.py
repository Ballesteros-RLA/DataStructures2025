from queue import LifoQueue

class StackQueue:
    def __init__(self):
        self.stack = LifoQueue()
    
    def push(self, item):
        self.stack.put(item)
    
    def pop(self):
        if not self.stack.empty():
            return self.stack.get()
        return "Stack is empty"
    
    def is_empty(self):
        return self.stack.empty()
    
    def size(self):
        return self.stack.qsize()


stack2 = StackQueue()
stack2.push("A")
stack2.push("B")
stack2.push("C")
print("Popped item:", stack2.pop())
print("Is stack empty?", stack2.is_empty())