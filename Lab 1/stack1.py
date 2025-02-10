class StackList:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        print("Stack (Top -> Bottom):", self.stack[::-1])


stack1 = StackList()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.display()
print("Popped item:", stack1.pop())
stack1.display()