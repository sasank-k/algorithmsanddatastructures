class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.__count = 0

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.__count
