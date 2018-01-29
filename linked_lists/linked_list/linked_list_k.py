""""""
class Node(object):
    """"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return self.data


class LinkedList(object):
    """"""
    def __init__(self, head=None):
        self.head = head
    
    def __len__(self):
        length = 0
        temp = self.head
        while temp is not None:
            length += 1
            temp = temp.next_node
        return length

    def insert_to_front(self, data):
        if data is None:
            return
        self.head = Node(data, self.head)
    
    def append(self, data):
        if data is None:
            return
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next_node is not None:
            temp = temp.next_node
        temp.next_node = Node(data)

    def find(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next_node
        return None

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next_node
            return
        temp = self.head
        while temp.next_node is not None:
            if temp.next_node.data == data:
                temp.next_node = temp.next_node.next_node
                return
            temp = temp.next_node
        return None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next_node

    def get_all_data(self):
        temp = self.head
        result = []
        while temp is not None:
            result.append(temp.data)
            temp = temp.next_node
        return result