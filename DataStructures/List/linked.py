class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class List:
    def __init__(self, head=None):
        self.head = head
        self.size = 0
        if self.head is not None:
            self.traverse()

    def traverse(self):
        if self.head is None:
            raise Exception("Empty list.")
        else:
            self.size = 0
            output = []
            current = self.head
            while current:
                output.append(current.val)
                self.size += 1
                current = current.nxt
        return output

    def insert(self, val, pos='after', item=None, indx=None):
        node = Node(val)
        if self.head:
            current = self.head
        else:
            self.head = node
            self.size = 1
            return

        if pos == 'after':
            if item is not None:
                while current:
                    if item == current.val:
                        node.nxt = current.nxt
                        current.nxt = node
                        self.size += 1
                        return
                    current = current.nxt
                raise Exception("Item not found.")
            elif indx is not None:
                while current and indx:
                    current = current.nxt
                    indx -= 1
                if current:
                    node.nxt = current.nxt
                    current.nxt = node
                    self.size += 1
                    return
                raise Exception("Index out of range.")
            else:
                while current.nxt:
                    current = current.nxt
                current.nxt = node
                self.size += 1
                return
        elif pos == 'before':
            if item is not None:
                if item == current.val:
                    self.head = Node(val,self.head)
                    self.size += 1
                    return
                elif current.nxt:
                    while current.nxt:
                        if current.nxt.val is item:
                            node.nxt = current.nxt
                            current.nxt = node
                            self.size += 1
                            return
                        current = current.nxt
                raise Exception("Item not found.")
            elif indx is not None:
                if indx == 0:
                    self.head = Node(val,self.head)
                    self.size += 1
                    return
                elif current.nxt:
                    indx -= 1
                    while current.nxt and indx:
                        current = current.nxt
                        indx -= 1
                    if current.nxt:
                        current.nxt = Node(val,current.nxt)
                        self.size += 1
                        return
                raise Exception("Index out of range.")
            else:
                self.head = Node(val,self.head)
                self.size += 1
                return
        else:
            raise Exception("Invalid position. Please use 'before' or 'after'.")

    def remove(self, pos='last', item=None, indx=None):
        if self.head is None:
            raise Exception("Empty list.")
        else:
            current = self.head

        if item is not None:
            if item == current.val:
                self.head = self.head.nxt
                self.size -= 1
                return
            else:
                while current.nxt:
                    if item == current.nxt.val:
                        current.nxt = current.nxt.nxt
                        self.size -= 1
                        return
                    current = current.nxt
            raise Exception ("Item not found.")
        elif indx is not None:
            if indx > 0:
                if current.nxt:
                    while current.nxt.nxt and indx:
                        current = current.nxt
                        indx -= 1
                    current.nxt = current.nxt.nxt
                    self.size -= 1
                    return
                else:
                    raise Exception("Index out of range.")
            else:
                self.head = self.head.nxt
        else:
            if pos == 'last':
                if current.nxt:
                    if current.nxt.nxt:
                        while current.nxt.nxt:
                            current = current.nxt
                        current.nxt = None
                        self.size -= 1
                        return
                    else:
                        self.head.nxt = None
                else:
                    self.head = None
            elif pos == 'first':
                self.head = self.head.nxt
                self.size -= 1
                return
            else:
                raise Exception("Invalid position. Please use 'first' or 'last'.")

if __name__ == '__main__':
    L = List()
    items = [3,2,1,9,8,7,6,5,4,0]
    for item in items:
        L.insert(item)

    L.insert(8,'after',7)
    L.insert(0,'after',indx=2)
    L.insert(4,'before',item=7)
    L.insert(5,'before',indx=5)
    assert L.traverse() == [3, 2, 1, 0, 9, 5, 8, 4, 7, 8, 6, 5, 4, 0]
    assert L.size == 14

    L.remove()
    L.remove('first')
    L.remove(item=7)
    L.remove(indx=5)
    assert L.traverse() == [2, 1, 0, 9, 5, 8, 8, 6, 5, 4]
    assert L.size == 10

    print("Pass")
