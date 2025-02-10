from queue import Queue

class QueueModuleExample:
    def __init__(self):
        self.queue = Queue()
    
    def enqueue(self, item):
        self.queue.put(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        if not self.queue.empty():
            item = self.queue.get()
            print(f"Dequeued: {item}")
            return item
        print("Queue is empty!")
        return None
    
    def is_empty(self):
        return self.queue.empty()


queue2 = QueueModuleExample()
queue2.enqueue(30)
queue2.enqueue(40)
queue2.dequeue()
queue2.dequeue()
queue2.dequeue()
