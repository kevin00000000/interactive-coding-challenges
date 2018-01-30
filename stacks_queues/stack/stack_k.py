class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack(object):
    def __init__(self, top=None):
        self.top = top
    
    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None