class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def traverse(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements


sll1 = SinglyLinkedList()
sll1.insert_at_end(10)
sll1.insert_at_end(20)
sll1.insert_at_end(30)
print("Example 1 - List after insertion at end:", sll1.traverse())
