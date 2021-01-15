class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class List:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def print_list(self):
        listToPrint = []
        current = self.head

        while current:
            listToPrint.append(current.val)
            current = current.next

        return listToPrint

    def insert(self, item):
        current = Node(item, self.head)

        while current.next:
            current = current.next

        if current.next != self.head:
            current.next = Node(item, current.next)
        else:
            self.head = current

        self.size += 1

    def insert_at_index(self, item, index):
        current = Node(item, self.head)

        while current.next and (index > 0):
            current = current.next
            index -= 1

        if index != 0:
            raise Exception("Index out of range.")

        if current.next != self.head:
            current.next = Node(item, current.next)
        else:
            self.head = current

        self.size += 1

    def insert_at_item(self, item, search):
        current = Node(item, self.head)

        while current.next and current.next.val != search:
            current = current.next

        if search and current.next.val != search:
            raise Exception("Item not found")

        if current.next != self.head:
            current.next = Node(item, current.next)
        else:
            self.head = current

        self.size += 1

    def remove(self, pos='last', item=None, indx=None):
        if self.head is None:
            raise Exception("Empty list.")
        else:
            current = self.head

        if item is not None:
            if item == current.val:
                self.head = self.head.next
                self.size -= 1
                return
            else:
                while current.next:
                    if item == current.next.val:
                        current.next = current.next.next
                        self.size -= 1
                        return
                    current = current.next
            raise Exception ("Item not found.")
        elif indx is not None:
            if indx > 0:
                if current.next:
                    while current.next.next and indx:
                        current = current.next
                        indx -= 1
                    current.next = current.next.next
                    self.size -= 1
                    return
                else:
                    raise Exception("Index out of range.")
            else:
                self.head = self.head.next
        else:
            if pos == 'last':
                if current.next:
                    if current.next.next:
                        while current.next.next:
                            current = current.next
                        current.next = None
                        self.size -= 1
                        return
                    else:
                        self.head.next = None
                else:
                    self.head = None
            elif pos == 'first':
                self.head = self.head.next
                self.size -= 1
                return
            else:
                raise Exception("Invalid position. Please use 'first' or 'last'.")

    @property
    def length(self):
        return self.size

if __name__ == '__main__':
    L = List()
    items = [3,2,1,9,8,7,6,5,4,0]

    for item in items:
        L.insert(item)

    assert L.print_list() == [3,2,1,9,8,7,6,5,4,0]
    assert L.length == 10

    G = List()

    G.insert_at_index(3,0)
    G.insert_at_index(2,1)
    G.insert_at_index(1,0)

    L.insert_at_index(0, 2)
    L.insert_at_index(2, 0)
    L.insert_at_index(4, 1)

    assert G.print_list() == [1,3,2]
    assert L.print_list() == [2,4,3,2,0,1,9,8,7,6,5,4,0]
    assert G.length == 3
    assert L.length == 13

    G = List()

    G.insert_at_item(3,0)
    G.insert_at_item(5,3)
    G.insert_at_item(7,5)
    G.insert_at_item(4,3)
    G.insert_at_item(9,5)

    L.insert_at_item(5, 5)
    L.insert_at_item(0, 0)
    L.insert_at_item(1, 1)

    assert G.print_list() == [7,9,5,4,3]
    assert L.print_list() == [2,4,3,2,0,0,1,1,9,8,7,6,5,5,4,0]
    assert G.length == 5
    assert L.length == 16

    L.remove()
    L.remove(item=7)
    L.remove(indx=5)
    assert L.print_list() == [2,4,3,2,0,0,1,9,8,6,5,5,4]
    assert L.size == 13

    print("Pass")
