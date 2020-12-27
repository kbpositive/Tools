class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class List:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        if self.head:
            current = self.head
            while current:
                print(current.val)
                current = current.nxt
        else:
            print("Empty list.")

    def insert(self, val, pos='after', item=None, indx=None):
        node = Node(val)
        if self.head:
            current = self.head
        else:
            self.head = node
            return

        if pos == 'after':
            if item is not None:
                while current:
                    if item == current.val:
                        node.nxt = current.nxt
                        current.nxt = node
                        return
                    current = current.nxt
                return "Item not found."
            elif indx is not None:
                while current and indx:
                    current = current.nxt
                    indx -= 1
                if current:
                    node.nxt = current.nxt
                    current.nxt = node
                    return
                return "Index out of range."
            else:
                while current.nxt:
                    current = current.nxt
                current.nxt = node
                return
        elif pos == 'before':
            if item is not None:
                if item == current.val:
                    self.head = Node(val,self.head)
                    return
                elif current.nxt:
                    while current.nxt:
                        if current.nxt.val is item:
                            node.nxt = current.nxt
                            current.nxt = node
                            return
                        current = current.nxt
                return "Item not found."
            elif indx is not None:
                if indx == 0:
                    self.head = Node(val,self.head)
                    return
                elif current.nxt:
                    indx -= 1
                    while current.nxt and indx:
                        current = current.nxt
                        indx -= 1
                    if current.nxt:
                        current.nxt = Node(val,current.nxt)
                        return
                return "Index out of range."
            else:
                self.head = Node(val,self.head)
                return
        else:
            return "Invalid position. Please use 'before' or 'after'."

    def remove(self, pos='last', item=None, indx=None):
        if self.head:
            current = self.head
        else:
            return

        if item is not None:
            if item == current.val:
                self.head = self.head.nxt
                return
            else:
                while current.nxt:
                    if item == current.nxt.val:
                        current.nxt = current.nxt.nxt
                        return
                    current = current.nxt
            return "Item not found."
        elif indx is not None:
            if indx > 0:
                if current.nxt:
                    while current.nxt.nxt and indx:
                        current = current.nxt
                        indx -= 1
                    current.nxt = current.nxt.nxt
                    return
                else:
                    return "Index out of range."
            else:
                self.head = self.head.nxt
        else:
            if pos == 'last':
                if current.nxt:
                    if current.nxt.nxt:
                        while current.nxt.nxt:
                            current = current.nxt
                        current.nxt = None
                        return
                    else:
                        self.head.nxt = None
                else:
                    self.head = None
            elif pos == 'first':
                self.head = self.head.nxt
                return
            else:
                return "Invalid position. Please use 'first' or 'last'."
# examples
l = List()
l.insert(1)
l.insert(1.25)
l.insert(0,'before')
l.insert(1.15,'after',1)
l.insert(0.75,'before',1)
l.insert(0.25,'after',indx=0)
l.insert(1.2,'after',indx=4)
l.insert(0.9,'before',indx=3)
l.remove(indx=2)
l.traverse()
