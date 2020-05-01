class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgnt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node:
                if self.current_node.left != None:
                    self.current_node.left = value
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node.right = value
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node == value:
                return True
            elif value < self.current_node:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
