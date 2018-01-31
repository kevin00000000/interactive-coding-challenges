class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
    
    def enqueue(self, data):
        if self.last is not None:
            self.last.next = Node(data)
            self.last = self.last.next
        else:
            self.last = Node(data)
            self.first = self.last

    def dequeue(self):
        if self.first is None:
            return None
        if self.first == self.last:
            data = self.first.data
            self.first = self.last = None
            return data
        data = self.first.data
        self.first = self.first.next
        return data
        
