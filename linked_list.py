class Node:
    def __init__(self, data, next=None):
        self.node = data
        self.next = next


class NodeManager:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
