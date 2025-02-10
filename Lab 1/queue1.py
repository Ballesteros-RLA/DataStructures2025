class QueueList:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            return item
        print("Queue is empty!")
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        print("Queue state:", self.queue)


queue1 = QueueList()
queue1.enqueue(10)
queue1.enqueue(20)
queue1.display()
queue1.dequeue()
queue1.display()
