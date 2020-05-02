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

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node == value:
                searched = True
                break
            elif value < self.current_node:
                self.parent = self.current_node
                self.current_node = self.current_node.right
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.left

        if searched == False:
            return False

        # leaf 노드 삭제하는 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        # 자식노드가 하나만 있는 노드를 삭제하는 경우
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.right
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
