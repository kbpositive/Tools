class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class List:
    def __init__(self, head=None):
        self.head = head

    def insert(self, val, pos=None):
        node = Node(val)
        current = self.head

        if pos:
            if self.head.val is pos:
                self.head = Node(val, self.head)
                return self.head
            while current.nxt:
                if current.nxt.val is pos:
                    node.nxt = current.nxt
                    current.nxt = node
                    return self.head
                current = current.nxt
            return "Position not found."
        else:
            if self.head is None:
                self.head = node
                return self.head
            while current.nxt:
                current = current.nxt
            current.nxt = node
